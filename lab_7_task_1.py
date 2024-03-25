from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def cicloida(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 8*np.pi, 0.1)
    x = x0 + R*(alpha-np.sin(alpha)**3)
    y = y0 + R*(1-np.cos(alpha)**3)
    return x, y

def animate(i):
    ball.set_data(cicloida(R=1, vx0=0.01, vy0=0.01, time=i))

if __name__=='__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

edge=10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    
ani = FuncAnimation(fig, animate, frames=100, interval=30)
 
ani.save('animation_4.1.gif')