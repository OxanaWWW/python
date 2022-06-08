
import numpy as np
from math import exp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#%matplotlib inline

def f(x, k=1, a=0, b=0):
    return k * np.cos(x-a) + b

x = np.linspace(0, 4*np.pi, 100)
plt.plot(x,f(x), color="red");
plt.plot(x,f(x, 2, a=0.3), color="green");
plt.plot(x,f(x, 2, b=1), color="blue");
plt.grid(True)
plt.show()