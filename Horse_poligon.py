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

points = []
for x_coord in np.linspace(*x_limits, pointsnumber):
    for y_coord in np.linspace(*y_limits, pointsnumber):
        p = geom.Point(x_coord, y_coord)
        if p.within(poly):
            plt.plot(x_coord, y_coord, 'go', ms=0.5)

plt.plot(x, y, 'bo')
plt.axis('equal')
plt.plot(spline_curve[0], spline_curve[1], 'g')
plt.savefig('Points_in_poligon.jpg')