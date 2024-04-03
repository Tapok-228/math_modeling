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


coords = circle(450, 100, 1100, -1.79, -0.5)
plt.plot(coords[0], coords[1], lw=2, color='w', zorder=1)


coords_1 = circle(260, 660, 665, 0.6, 2.5)
plt.plot(coords_1[0], coords_1[1], lw=2, color='w', zorder=1)

plt.plot([878, 890], [805, 630], lw=2, color='w', zorder=1)

coords_3 = circle(50, 940, 615, 3.05, 4.05)
plt.plot(coords_3[0], coords_3[1], lw=2, color='w', zorder=1)

coords_4 = circle(150, 770, 500, 6.8, 8)
plt.plot(coords_4[0], coords_4[1], lw=2, color='w', zorder=1)

coords_5 = circle(50, 740, 600, 1.4, 4.9)
plt.plot(coords_5[0], coords_5[1], lw=2, color='w', zorder=1)

coords_6 = circle(100, 770, 450, 6, 8.1)
plt.plot(coords_6[0], coords_6[1], lw=2, color='w', zorder=1)

coords_7 = circle(250, 1040, 230, 1.5, 2.4)
plt.plot(coords_7[0], coords_7[1], lw=2, color='w', zorder=1)

coords_8 = circle(150, 1025, 625, 4.7, 6.5)
plt.plot(coords_8[0], coords_8[1], lw=2, color='w', zorder=1)

plt.plot([1175, 1140], [630, 940], lw=2, color='w', zorder=1)

coords_10 = circle(55, 1083, 945, 6.4, 7.9)
plt.plot(coords_10[0], coords_10[1], lw=2, color='w', zorder=1)

plt.plot([1080, 1070], [1000, 1080], lw=2, color='w', zorder=1)

plt.plot([1079, 1170], [1085, 1115], lw=2, color='w', zorder=1)

plt.plot([1170, 1210], [1115, 1280], lw=2, color='w', zorder=1)

coords_14 = circle(170, 1373, 1230, 1.2, 3)
plt.plot(coords_14[0], coords_14[1], lw=2, color='w', zorder=1)

plt.plot([1440, 1710], [1385, 1270], lw=2, color='w', zorder=1)

coords_16 = circle(200, 1802, 1448, -2, -0.9)
plt.plot(coords_16[0], coords_16[1], lw=2, color='w', zorder=1)


plt.savefig('new_horse.png')