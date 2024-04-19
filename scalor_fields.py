import matplotlib.pyplot as plt
import numpy as np
import random

fig, ax = plt.subplots()
N = 1000
x, y = np.zeros(N), np. zeros(N)

for i in range(N):
    x[i] = random.uniform(0, 1)
    y[i] = random.uniform(0, 1)


scalor_fields = 50 * np.sqrt(x**2 + y**2)

sc_plot = ax.scatter(x, y, c=scalor_fields)
cbar = fig.colorbar(sc_plot)
cbar.set_label('Скалярное поле температуры, °C')

plt.savefig('scalor_fields.png')