from math import e, pi
import matplotlib.pyplot as plt
import numpy as np

def log_spir(b=1, x0=0, y0=0):

    nu = np.arange(0, 8*pi, 0.1)

    r = e**(b*nu)
    x = np.arange(, , 0.1)
    y = np.arange(, , 0.1)

    plt.plot(x, y)
    plt.axis('equal')

    plt.savefig('task4.png')

log_spir()