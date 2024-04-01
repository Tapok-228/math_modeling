from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def cicloida(R=3):
    alpha = np.arange(0, 8*np.pi, 0.1)
    x = R*np.cos(alpha)**3
    y = R*np.sin(alpha)**3
    
    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_3_lab_7.png')

if __name__=='__main__':
    cicloida()