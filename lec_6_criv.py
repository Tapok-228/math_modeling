import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0):

    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
    plt.plot(x, y)

    plt.savefig('fig_4.png')

if __name__ == '__main__':
    parabola_plotter()