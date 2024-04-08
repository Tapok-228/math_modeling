import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom


phi = np.linspace(0, 2*np.pi, 40)
r = 0.5 + np.cos(phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

coords = []
for i in range(len(spline_curve[0])):
    coords.append([spline_curve[0][i], spline_curve[1][i]])

poly = geom.Polygon(coords)
pointsnumber = 100
x_limits = [-0.5, 2]
y_limits = [-1, 1]

points_x, points_y = [], []
for x_coord in np.linspace(*x_limits, pointsnumber):
    for y_coord in np.linspace(*y_limits, pointsnumber):
        p = geom.Point(x_coord, y_coord)
        if p.within(poly):
            points_x.append(x_coord)
            points_y.append(y_coord)

x = np.array(points_x)
y = np.array(points_y)
t = 5*np.sin((np.sqrt((x-0.75)**2+y**2)+1)/0.05)  # закон закрашивания

points = ax.scatter(points_x, points_y, c=t)  # ставит точки
c_bar = fig.colorbar(points)
plt.savefig('crendel.png')