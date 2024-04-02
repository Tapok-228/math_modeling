import matplotlib.pyplot as plt
import numpy as np

becgraund='Horse.jpg'
img = plt.imread(becgraund)
plt.imshow(img, zorder=0)


def circle(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

def parab(a, b, c, x0, x1, y0):
    x = np.arange(x0, x1, 0.1)
    y = (a*x)**2+b*x+c+y0
    return x, y

def line(x0, x1, y0, y1):
    
    return x, y

coords = circle(450, 100, 1100, -2, -0.5)
plt.plot(coords[0], coords[1], lw=1, color='w', zorder=1)


coords_1 = circle(260, 660, 665, 0.6, 2.5)
plt.plot(coords_1[0], coords_1[1], lw=1, color='w', zorder=1)


coords_2 = line()
plt.plot(coords_2[0], coords_2[1], lw=1, color='w', zorder=1)

coords_5 = circle(50, 740, 600, 1, 5)
plt.plot(coords_5[0], coords_5[1], lw=1, color='w', zorder=1)


plt.savefig('new_horse.png')