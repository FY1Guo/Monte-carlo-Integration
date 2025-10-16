import numpy as np
import matplotlib.pyplot as plt


rng = np.random.default_rng()

a = 5
b = 2

def area(N, rng=rng):
    Abox = 4*a*b
    x = rng.random(-a, a, size=N)
    y = rng.random(-b, b, size=N)
    inside = (x/a)**2 + (y/b)**2 <= 1
    A = Abox * np.sum(inside) / N**2
    return A



theta_list = np.linspace(0, 2*np.pi, 101)
x_list = a*np.cos(theta_list)
y_list = b*np.sin(theta_list)

plt.plot(x_list, y_list)
plt.grid()
plt.show()
