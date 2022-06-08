import numpy as np
from math import exp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#%matplotlib inline

#Решите систему уравнений: y = x**2 – 1; exp(x) + x∙(1 – y) = 1

point_count = 200
x = np.append(np.linspace(-2, 0.00001, point_count//2), np.linspace(0.00001, 4.5, point_count//2))
y = np.linspace(-2, 20, point_count)

x0 = np.array([0]*point_count)
y0 = np.array([0]*point_count)

y1 = x**2 - 1
y2 = np.exp(x)/x + 1 -1/x

plt.plot(x,y1, color="green")
plt.plot(x,y2, color="blue")

plt.plot(x,y0, color="red", linestyle='--', linewidth=1)
plt.plot(x0,y, color="red",linestyle='--', linewidth=1)

plt.grid(True)

def equations(p):
    x, y = p
    return (x**2-1-y, exp(x)+x*(1-y)-1)

chunks = [(-2, -1), (-0.1, 0.1), (2.5, 3), (4, 4.5)]

for (x_from, x_to) in chunks:
    x, y = fsolve(equations, (x_from, x_to))
    print('{:.6f}'.format(x), '{:.6f}'.format(y))
plt.show()