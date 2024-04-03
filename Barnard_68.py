import matplotlib.pyplot as plt
import numpy as np

becgraund='Barnard-68.jpg'
img = plt.imread(becgraund)
plt.imshow(img, zorder=0)


def circle(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y


coords = circle(470, 1050, 990, 3.9, 8.3)
plt.plot(coords[0], coords[1], lw=2, color='w', zorder=1)

plt.plot([705, 760], [675, 1150], lw=2, color='w', zorder=1)

coords_2 = circle(75, 688, 1175, 6, 7.6)
plt.plot(coords_2[0], coords_2[1], lw=2, color='w', zorder=1)

plt.plot([700, 540], [1255, 1350], lw=2, color='w', zorder=1)

coords_3 = circle(130, 600, 1465, 1, 4.3)
plt.plot(coords_3[0], coords_3[1], lw=2, color='w', zorder=1)

plt.plot([680, 890], [1570, 1430], lw=2, color='w', zorder=1)
plt.savefig('new_Barnard_68.png')