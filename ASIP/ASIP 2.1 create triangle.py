from scipy import signal
import matplotlib.pyplot as plot
import numpy as np
t = np.linspace(0,1,500)
plot.plot(t,signal.sawtooth(2*np.pi*3*t,0.5))
plot.xlabel('time')
plot.ylabel('Amplitude')
plot.title('Triangle Signal')
plot.show()
