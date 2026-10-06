import numpy as np
n_list = [10, 100, 1000, 10000]
p = 0.7


for n in n_list:
    errors = []
    for epoch in range(1000):
        x = np.random.binomial(1, p, size=n)

        p_hat = np.mean(x)

        error = abs(p_hat - p)

        errors.append(error)

    print(n,np.mean(errors))