from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)**2
    y = R * np.sin(alpha)
    return x, y

def animate(i):
    ball.set_data(circle_move(R=2, angle_vel=1, time=i))

if __name__=='__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames = 180, interval=30)

    ani.save('animation_2.gif')
