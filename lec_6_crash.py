import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]
plt.plot(x, y, color='g', label='Graf 1', marker='>', ms=5)
plt.plot(y, x, color='b', label='Graf 2', marker='o', ms=3)

plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('fig_3.png')