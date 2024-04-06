import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

becgraund='Horse.jpg'
img = plt.imread(becgraund)
plt.imshow(img, zorder=0)

def circle(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

coords = circle(450, 100, 1100, -1.79, -0.5)
plt.plot(coords[0], coords[1], lw=2, color='w', zorder=1)

coords_1 = circle(260, 660, 665, -5.7, -3.8)
plt.plot(coords_1[0], coords_1[1], lw=2, color='w', zorder=1)

         
x = np.append(coords[0], coords_1[0])
y = np.append(coords[1], coords_1[1])


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('Horse_splain.png')