import numpy as np

np.random.seed(42)

p = 0.3

samples = np.random.binomial(1,p,10000)

print("sample mean:", np.mean(samples))
print("sample variance:", np.sum((samples - np.mean(samples)) ** 2) / 10000)#np.var(samples)
print("theoretical mean:", 0.3)
print("theoretical variance:", 0.21)

samples = np.random.binomial(10,0.3,10000)

print("sample mean:", np.mean(samples))
print("sample variance:", np.var(samples))
print("theoretical mean:", 3000)
print("theoretical variance:", 2100)