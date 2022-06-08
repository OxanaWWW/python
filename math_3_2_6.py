#ellipse*************
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib
# inline


# эллипс
def draw_ellipse(a=2, b=1, x0=0, y0=0, color='C1'):
    angle = np.linspace(0, 2 * np.pi, 360)

    x = np.add(a * np.cos(angle), x0)
    y = np.add(b * np.sin(angle), y0)

    plt.plot(x, y, color=color, linewidth=1)
    plt.gca().set_aspect('equal')


draw_ellipse(x0=1, y0=2)
plt.show()