import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

becgraund='Meshok.jpg'
img = plt.imread(becgraund)
plt.imshow(img, zorder=0)

def circle(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

def circle_r(R, x0, y0, t0, t1):
    t=np.arange(t1, t0, -0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

coords_line = np.array([[870, 890], [805, 630]])
coords_line_1 = np.array([[1000, 1200], [805, 630]])
x = np.append(coords_line[0], coords_line_1[0])
y = np.append(coords_line[1], coords_line_1[1])













spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('Meshok_splain.png')