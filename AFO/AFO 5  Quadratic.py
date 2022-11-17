import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
ones = np.ones(3)
A = np.array( ((0,1),(1,1),(2,1)))
xfeature = A.T[0]
squaredfeature = A.T[0] ** 2
b = np.array( (1,2,0), ndmin=2 ).T
b = b.reshape(3)
features = np.concatenate((np.vstack(ones), np.vstack(xfeature), np.vstack(squaredfeature)), axis = 1)
featuresc = features.copy()
print(features)
m_det = np.linalg.det(features)
print(m_det)
determinants = []

for i in range(3):
    featuresc.T[i] = b
    print(featuresc)
    det = np.linalg.det(featuresc)
    determinants.append(det)
    print(det)
    featuresc = features.copy()
determinants = determinants / m_det
print(determinants)
plt.scatter(A.T[0],b)
u = np.linspace(0,3,100)
plt.plot(u, u**2*determinants[2] + u*determinants[1] + determinants[0] )
p2 = np.polyfit(A.T[0],b,2)
plt.plot(u, np.polyval(p2,u), 'b--')
plt.show()

