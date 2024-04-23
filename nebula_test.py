import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom
import h5py
import random

phi = np.linspace(0, 2*np.pi, 40)
R = 0.5 + np.cos(phi)
x = R*np.cos(phi)
y = R*np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 500
x_pictures_limits = [-0.5, 2]
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

def bell_function(x, y, intensity=1, dec_rate=[5, 5]):
    scalor_func = intensity * np.exp(-dec_rate[0]*(x-0.8)**2-dec_rate[1]*(y-0)**2)
    return scalor_func

##############################################
float_type = np.float64
int_type = np.int32

picture_size_x = max(x_pictures_limits) - min(x_pictures_limits)
picture_size_y = max(y_pictures_limits) - min(y_pictures_limits)
picture_size = max(picture_size_x, picture_size_y)
box_size = 100 * picture_size

gas_part_num = len(x_p)
gas_coords = np.zeros([gas_part_num, 3], dtype=float_type)
gas_vel = np.zeros([gas_part_num, 3], dtype=float_type)
# gas_masses = np.zeros(len(x_p))
gas_masses_0 = 2*1.6735575e-24 * 2*10**5 * 0.175*9.460e17 / (2*10**(-3))
gas_masses = bell_function(x_p, y_p, gas_masses_0)

for i in range(len(x_p)):
    gas_coords[i][0] = x_p[i] / picture_size + box_size/2
    gas_coords[i][1] = y_p[i] / picture_size + box_size/2

    gas_vel[i, 0] = float_type(0.001)
    gas_vel[i, 1] = float_type(0.0)

    
    

# gas_masses_0 = 2*1.6735575e-24 * 2*10**5 * 0.175*9.460e17 / (2*10**(-3))
# gas_masses = np.full(gas_part_num, gas_masses_0, dtype=float_type)

##############################################
background_parts = 5000

bg_coords = np.zeros([background_parts, 3], dtype=float_type)
for i in range(background_parts):
    bg_coords[i, 0] = float_type(random.uniform(0, box_size))
    bg_coords[i, 1] = float_type(random.uniform(0, box_size))

bg_velocity = np.zeros([background_parts, 3], dtype=float_type)
background_masses_0 = 0.000001 * gas_masses_0
bg_mass =  np.full(background_parts, background_masses_0, dtype=float_type)

all_parts = gas_part_num + background_parts
all_coords = np.zeros([all_parts, 3], dtype=float_type)
all_velocity = np.zeros([all_parts, 3], dtype=float_type)

for i in range(all_parts):
    if i < gas_part_num:
        all_coords[i, :] = gas_coords[i, :]
        all_velocity[i, :] = gas_vel[i, :]
    else:
        all_coords[i, :] = bg_coords[i-gas_part_num, :]
        all_velocity[i, :] = bg_velocity[i-gas_part_num, :]

all_mass = np.append(gas_masses, bg_mass)

##############################################
IC = h5py.File('IC_2.hdf5', 'w')
header = IC.create_group("Header")
part0 = IC.create_group("PartType0")

KEY_STUB = 0
KEY_STUB_ARRAY = np.ones(6, dtype = int_type)
num_part = np.array([all_parts, 0, 0, 0, 0, 0], dtype=int_type)
header.attrs.create("NumPart_ThisFile", num_part)
header.attrs.create("NumPart_Total_HighWord", np.zeros(6, dtype=int_type))
header.attrs.create("NumPart_Total", num_part)
header.attrs.create("MassTable", KEY_STUB_ARRAY)
header.attrs.create("Time", KEY_STUB)
header.attrs.create("BoxSize", KEY_STUB)
header.attrs.create("Redshift", KEY_STUB)
header.attrs.create("Omega0", KEY_STUB)
header.attrs.create("OmegaB", KEY_STUB)
header.attrs.create("OmegaLambda", KEY_STUB)
header.attrs.create("HubbleParam", KEY_STUB)
header.attrs.create("Flag_Sfr", KEY_STUB)
header.attrs.create("Flag_Cooling", KEY_STUB)
header.attrs.create("Flag_StellarAge", KEY_STUB)
header.attrs.create("Flag_Metals", KEY_STUB)
header.attrs.create("Flag_Feedback", KEY_STUB)
header.attrs.create("NumFilesPerSnapshot", KEY_STUB)
header.attrs.create("Flag_DoublePrecision", 1)

part0.create_dataset("ParticleIDs", data=np.arange(0, all_parts))
part0.create_dataset("Coordinates", data=all_coords)
part0.create_dataset("Velocities", data=all_velocity)
part0.create_dataset("Masses", data=all_mass)

IC.close()