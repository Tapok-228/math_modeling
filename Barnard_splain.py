import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

becgraund='Barnard-68.jpg'
img = plt.imread(becgraund)
plt.imshow(img, zorder=0)

def circle(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

coords = circle(470, 1050, 990, 3.9, 8.3)
plt.plot(coords[0], coords[1], lw=2, color='w', zorder=1)

plt.plot([705, 760], [675, 1150], lw=2, color='w', zorder=1)

coords_line = np.array([[705, 760], [675, 1150]])

x = np.append(coords_line[0], coords[0])
y = np.append(coords_line[1], coords[1])

coords_line_2 = np.array([[680, 890], [1570, 1430]])

x = np.append(x, coords_line_2[0])
y = np.append(y, coords_line_2[1])


coords_3 = circle(130, 600, 1465, 1, 4.3)
plt.plot(coords_3[0], coords_3[1], lw=2, color='w', zorder=1)

x = np.append(x, coords_3[0])
y = np.append(y, coords_3[1])


coords_line_4 = np.array([[700, 540], [1255, 1350]])

x = np.append(x, coords_line_4[0])
y = np.append(y, coords_line_4[1])


t=np.arange(7.6, 6, -0.1)
x_1 = 75 * np.cos(t)+688
y_1 = 75 * np.sin(t)+1175

x = np.append(x, x_1)
y = np.append(y, y_1)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('new_Barnard_68_splain.png')