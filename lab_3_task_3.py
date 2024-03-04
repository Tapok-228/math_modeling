import numpy as np

g=9.8

x0, y0 = int(input('Введите координату X:')), int(input('Введите координату Y:'))
v = int(input('Задайте скорость:'))

itog = [[t, x0+v*t, y0+v*t-g*t**2/2] for t in np.arange(0, 5.1, 0.1)]
massiv = np.array(itog)

print(massiv)