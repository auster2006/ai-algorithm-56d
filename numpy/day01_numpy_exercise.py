import numpy as np
X = np.random.randn(100,20)
W = np.random.randn(20,10)
b = np.random.randn(10)

Y = X @ W + b

print(X.shape)
print(W.shape)
print(b.shape)
print(Y.shape)