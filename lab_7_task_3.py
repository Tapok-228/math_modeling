import matplotlib.pyplot as plt
import numpy as np

becgraund='kon.jpg'
img = plt.imread(becgraund)
plt.imshow(img, zorder=0)


def ris(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

coords = ris(50, 600, 800, 0, np.pi)
plt.plot(coords[0], coords[1], lw=3, color='w', zorder=1)

x=np.arange(0, 600, 0.1)
y=np.ones(len(x))*600

plt.plot(x, y, lw=3, color='w', zorder=1)



plt.savefig('new_kon.png')