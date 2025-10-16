import numpy as np
import matplotlib.pyplot as plt


rng = np.random.default_rng()

a = 5
b = 2

def area(N, rng=rng):
    area_box = 4*a*b
    x = rng.uniform(-a, a, size=N)
    y = rng.uniform(-b, b, size=N)
    inside = (x/a)**2 + (y/b)**2 <= 1
    p = inside.mean()
    area = area_box * p
    se = area_box * np.sqrt(p*(1-p)/N)
    return area, se


Ns = np.linspace(10, 10000, 100).astype(int)
area_est, area_err = [], []

for N in Ns:
    A = area(N, rng)
    area_est.append(A[0])
    area_err.append(A[1])
    
area_ana = np.pi*a*b

plt.figure()
plt.plot(Ns, area_est, 'o-', label="MC estimate")
plt.axhline(area_ana, color='k', label="analytic")
plt.xlabel("N samples")
plt.ylabel("Area")
plt.title("Area of ellipse")
plt.legend()
plt.grid()
plt.savefig("ellipse_area.png")
plt.show()


plt.figure()
plt.plot(Ns, area_err, 'o-')
plt.xlabel("N samples")
plt.ylabel("Error in area")
plt.title("Error in area of ellipse")
plt.grid()
plt.savefig("ellipse_area_error.png")
plt.show()


# theta_list = np.linspace(0, 2*np.pi, 101)
# x_list = a*np.cos(theta_list)
# y_list = b*np.sin(theta_list)

# plt.plot(x_list, y_list)
# plt.grid()
# plt.show()
