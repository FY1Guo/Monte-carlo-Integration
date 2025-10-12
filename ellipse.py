import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 2
theta_list = np.linspace(0, 2*np.pi, 101)
x_list = a*np.cos(theta_list)
y_list = b*np.sin(theta_list)

plt.plot(x_list, y_list)
plt.grid()
plt.show()
