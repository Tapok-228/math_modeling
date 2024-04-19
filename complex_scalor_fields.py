import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom


phi = np.linspace(0, 2*np.pi, 100)
R = 1
x = R*np.cos(phi)
y = R*np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 100
x_pictures_limits = [-1, 1]
y_pictures_limits = [-1, 1]

points_coords = []
for x_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_coord, y_coord)
        if p.within(polygon):
            points_coords.append(x_coord)
            points_coords.append(y_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate = [0.5, 0.5]):
    scalor_func = intensity * np.exp(-dec_rate[0]*x**2-dec_rate[1]*y**2)
    return scalor_func


intensity_center_x = [-0.5, 0.5, -0.4, 0, 0.4]
intensity_center_y = [0.3, 0.3, -0.5, -0.7, -0.5]
intensity_values = [5, 5, 3, 1, 3]

def scalor_function(x, y, intensity_center_x, intensity_center_y, intensity_values):
    scalor_field = 0.0
    for  i in range(len(intensity_center_x)):
        scalor_field += intensity_values[i]*bell_function(x-intensity_center_x[i], y-intensity_center_y[i], 30, [5,5])
    return scalor_field

scalor_fields = []
for i in range(len(x_p)):
    calculate = scalor_function(x_p[i], y_p[i], intensity_center_x, intensity_center_y, intensity_values)
    scalor_fields.append(calculate)

fig, ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c=scalor_fields)
cbar = fig.colorbar(sc_plot)
cbar.set_label('Функция Белла')

plt.savefig('complex_scalor_fields.png')