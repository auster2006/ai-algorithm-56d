import numpy as np

n = 100
x = np.random.rand(n)*10-5
noise = np.random.randn(n)
w = 0
b = 0
y = 3*x + 2 + noise
lr = 0.01

for epoch in range(1000):
    y_pred = w * x + b
    loss = np.mean((y_pred-y)**2)
    dw = np.sum((2*x*(y_pred-y)))/n
    db = np.sum(2*(y_pred-y))/n
    w -= lr * dw
    b -= lr * db

y_pred = w * x + b
loss = np.mean((y_pred-y)**2)

print(w)
print(b)
print(loss)
