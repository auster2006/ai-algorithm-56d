import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.uniform(-5,5,100)#不知道怎么控制范围

true_w = 3
true_b = 2

noise = np.random.normal(0,1,100)#不知道正态怎么写

y = x * true_w + true_b + noise
w = 0
b = 0
lr = 0.1
loss_history = []

def predict(x, w, b):
    return(x *w + b)





def mse(y, y_pred):
    return(np.mean((y - y_pred) ** 2))



def gradients(x, y, y_pred):
    n = len(x)

    dw = 2 * np.sum(x * (y_pred - y)) / n
    db = 2 * np.sum((y_pred - y)) / n

    return dw, db




for epoch in range(100):
    y_pred = predict(x, w, b)
    loss = mse(y, y_pred)
    dw, db = gradients(x, y, y_pred)
    w = w - lr * dw
    b = b - lr * db
    loss_history.append(loss)

y_pred = predict(x, w, b)
loss = mse(y, y_pred)
loss_history.append(loss)

print(loss)
print(y_pred[:5])
print("dw =", dw)
print("db =", db)
print("new w =", w)
print("new b =", b)

m = np.ones((100,))
A = np.column_stack((x,m))
print(A.shape)
print(A[:5])

solution, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

w_lstsq = solution[0]
b_lstsq = solution[1]

print("lstsq w =", w_lstsq)
print("lstsq b =", b_lstsq)

print("GD w =", w)
print("GD b =", b)
