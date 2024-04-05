import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

t = np.linspace(0, 7, 20)
R=2
x = R * np.cos(t)
y = R * np.sin(t)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)

# figure_spline_part = np.arange(0, 1, 0.01)

spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(x, y, 'bo')

plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.axis('equal')
plt.savefig('pic_1.png')