#giperbola***********
# import matplotlib.pyplot
# import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib inline

from matplotlib import pyplot as plt
import numpy as np

#matplotlib.pyplot.show()
# гипербола
def draw_hyperbola(a=1, b=1, x_range=[-5, 5], color='C1'):
    epsilon = np.finfo(float).eps
    f0 = epsilon + a
    _x1 = np.linspace(x_range[0], -f0, (x_range[1] - x_range[0]) * 100)
    _x2 = np.linspace(f0, x_range[1], (x_range[1] - x_range[0]) * 100)

    f = lambda x: np.sqrt((x ** 2 / a ** 2) - 1) / b

    _y1 = np.array([f(v) for v in _x1])
    _y2 = np.array([f(v) for v in _x2])
    _y3 = np.array([-f(v) for v in _x1])
    _y4 = np.array([-f(v) for v in _x2])

    plt.plot(_x1, _y1, color=color, linewidth=1)
    plt.plot(_x2, _y2, color=color, linewidth=1)
    plt.plot(_x1, _y3, color=color, linewidth=1)
    plt.plot(_x2, _y4, color=color, linewidth=1)
    plt.gca().set_aspect('equal')
    plt.show()


draw_hyperbola()