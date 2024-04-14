import numpy as np

g = 9.8

x0, y0, v0 = float(input('Введите начальное положение по X:')), float(input('Введите начальное положение по Y:')), float(input('Введите начальную скорость:'))

itog = [['{:.1f}'.format(float(t)), '{:.1f}'.format(x0+v0*int(t)), '{:.1f}'.format(y0+v0*t-g*int(t)**2/2)] for t in np.arange(0, 5.1, 0.1)] #result = '{:.4f}'.format(number)

mass = np.array(itog)

print(mass)