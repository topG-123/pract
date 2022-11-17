import matplotlib.pylab as plt
import numpy as np
import GPy
import GPyOpt
import seaborn as sns
noise_var = 1e-6
n_samples = 1
def generate_noisy_points(n=10, noise_variance=1e-6):
  np.random.seed(777)
  X = np.random.uniform(-3., 3., (n, 1))
  y = np.sin(X) + np.random.randn(n, 1) * noise_variance**0.5
  return X, y
def kernel(x, y, l2=4):
  sqdist = np.sum(x**2,1).reshape(-1,1) + \
  np.sum(y**2,1) - 2*np.dot(x, y.T)
  return np.exp(-.5 * (1/l2) * sqdist)
X, y = generate_noisy_points()
plt.plot(X, y, 'x')
plt.show()
Xtest, ytest = generate_noisy_points(100)
Xtest.sort(axis=0)
N, n = len(X), len(Xtest)
K = kernel(X, X)
L = np.linalg.cholesky(K + noise_var*np.eye(N))
K_ = kernel(Xtest, Xtest)
Lk = np.linalg.solve(L, kernel(X, Xtest))
mu = np.dot(Lk.T, np.linalg.solve(L, y))
L = np.linalg.cholesky(K_ + noise_var*np.eye(n) - np.dot(Lk.T, Lk))
f_post = mu.reshape(-1,1) + np.dot(L, np.random.normal(size=(n,n_samples)))
n = len(Xtest)
K = kernel(Xtest, Xtest)
L = np.linalg.cholesky(K + 1e-6*np.eye(n))
f_prior = np.dot(L, np.random.normal(size=(n, n_samples)))
def posterior(X, Xtest, l2=0.1, noise_var=1.6):
  # compute the mean at our test points.
  N, n = len(X), len(Xtest)
  K = kernel(X, X, l2)
  L = np.linalg.cholesky(K + noise_var*np.eye(N))
  Lk = np.linalg.solve(L, kernel(X, Xtest, l2))
  mu = np.dot(Lk.T, np.linalg.solve(L, y))
  # compute the variance at our test points.
  K_ = kernel(Xtest, Xtest, l2)
  sd = np.sqrt(np.diag(K_) - np.sum(Lk**2, axis=0))
  return (mu, sd)
mu, sd = posterior(X, np.array([[1]]))
print(mu, sd)
sigma_f, l = 1.5, 2
kernel = GPy.kern.RBF(1, sigma_f, l)
sns.heatmap(kernel.K(X, X))
plt.show()
X, y = generate_noisy_points(noise_variance=0.01)
model = GPy.models.GPRegression(X,y,kernel)
mean, variance = model.predict(np.array([[1]]))
print(mean, variance)
print(model)
model.plot()
plt.show()
