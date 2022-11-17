from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()
x = np.arange(128) / 128
sig = np.sin(2* np.pi*x)
sig_noise = sig+rng.standard_normal(len(sig))
corr = signal.correlate(sig_noise, sig)
lags = signal.correlation_lags(len(sig), len(sig_noise))
corr /= np.max(corr)
fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, figsize = (4.8, 4.8))
ax_orig.plot(sig)
ax_orig.set_title("Original Signal")
ax_orig.set_xlabel("Sample Signal")
ax_noise.plot(sig_noise)
ax_noise.set_title("Signal With Noise")
ax_noise.set_xlabel("Sample Number")
ax_corr.plot(lags, corr)
ax_corr.set_title("Correlated Signal")
ax_corr.set_xlabel("Lag")
ax_orig.margins(0, 0.1)
ax_noise.margins(0, 0.1)
ax_corr.margins(0, 0.1)
fig.tight_layout()
plt.show()
