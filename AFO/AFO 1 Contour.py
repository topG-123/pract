import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(0, 10, 1)
y_axis = np.arange(0, 20, 2)

[x, y] = np.meshgrid(x_axis, y_axis)
fig, ax = plt.subplots(1, 1)
z = np.cos(x/2) + np.sin(y/4)

ax.contour(x, y, z)
ax.set_title('Contour Plot')
ax.set_xlabel('arrange_x')
ax.set_ylabel('arrange_y')

plt.show()
