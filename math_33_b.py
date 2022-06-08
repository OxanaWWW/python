import numpy as np
from math import exp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#% matplotlib
#inline


def cart_to_polar(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    a = np.arctan2(y, x)
    return (a, r)


def draw_circle_in_polar(r=1):
    angle = np.linspace(0, 2 * np.pi, 360)
    plt.polar(angle, r + np.zeros(np.size(angle)))


draw_circle_in_polar(1.4)
plt.show()