#ring***************
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib
# inline
from matplotlib import pyplot as plt
import numpy as np


# окружность
def draw_circle(r=1, x0=0, y0=0, color='C1'):
    angle = np.linspace(0, 2 * np.pi, 360)

    x = np.add(r * np.cos(angle), x0)
    y = np.add(r * np.sin(angle), y0)

    plt.plot(x, y, color=color, linewidth=1)
    plt.gca().set_aspect('equal')


draw_circle(x0=1, y0=2)

plt.show()