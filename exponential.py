import numpy as np
import matplotlib.pyplot as plt


rng = np.random.default_rng(0)

# inverse CDF

def pdf(x, lambd=1.0):
    return np.exp(-lambd * x) / (1 - np.exp(-lambd))


def cdf(x, lambd=1.0):
    return (1 - np.exp(-lambd * x)) / (lambd * (1 - np.exp(-lambd)))


def inverse_cdf(n, lambd=1.0):
    u = rng.random(n)
    return -np.log(1 - u * lambd * (1 - np.exp(-lambd))) / lambd


# rejection sampling

def rej_exp01(n, lambd=1.0):
    out = []
    while len(out) < n:
        x = rng.random()
        u = 2*rng.random()
        if u <= pdf(x, lambd):
            out.append(x)
    return np.array(out)


xs = np.linspace(0, 1, 400)
for sampler, name in [(inverse_cdf, "inverse-CDF"), (rej_exp01, "rejection")]:
    s = sampler(50000)
    plt.figure()
    plt.hist(s, bins=60, density=True, label=f"{name} samples")
    plt.plot(xs, pdf(xs), label="target pdf")
    plt.title(f"Exp on [0,1]: {name}")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("density")
    plt.savefig(f"exp_{name}.png")
plt.show()
