import matplotlib.pyplot as plt
import numpy as np

def elips(a=2, b=1):

    X1, X2 = int(input('Введите первый предел по Х:')), int(input('Введите второй предел по Х:'))
    n = int(input('Введите количество частей:'))

    x = np.linspace(X1, X2, n, endpoint=False)
    y1 = ((1-x**2/a**2)*b**2)**0.5
    y2 = -((1-x**2/a**2)*b**2)**0.5

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.axis('equal')

    plt.savefig('task3.png')

elips()