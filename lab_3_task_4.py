import numpy as np
import math

n, m = int(input('Введите параметр N:')), int(input('Введите параметр M:'))

triganometry_array = np.array([[math.sin(m*i+n*j+1) for i in range(m)] for j in range(n)])

for i in range(n):
    for j in range(m):
        if triganometry_array[i, j] < 0:
            triganometry_array[i, j] = 0

print(triganometry_array)