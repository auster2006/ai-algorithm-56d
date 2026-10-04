import numpy as np

np.random.seed(42)
n = 100000
lam = 4

poisson_samples = np.random.poisson(lam, n)

exp_samples = np.random.exponential(
    scale=1/lam,
    size=n
)

print("poisson_mean=", np.mean(poisson_samples))
print("poisson_var=", np.var(poisson_samples))
print("exp_mean=", np.mean(exp_samples))
print("exp_mean=", np.var(exp_samples))