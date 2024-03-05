import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0):

    X1, X2 = int(input('Введите первый предел по Х:')), int(input('Введите второй предел по Х:'))
    n = int(input('Введите количество частей:'))

    x = np.linspace(X1, X2, n)
    y = a*x**2 + b*x + c
    plt.plot(x, y)

    plt.savefig('task2.png')

parabola_plotter()