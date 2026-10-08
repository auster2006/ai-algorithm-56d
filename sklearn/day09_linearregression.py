import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)

x = np.random.uniform(-5, 5, 100)
noise = np.random.normal(0, 1, 100)
y = 3 * x + 2 + noise
y_outlier = y.copy()
y_outlier[0] += 100

A = np.column_stack((x,np.ones(len(x))))
paras, _, _, _, = np.linalg.lstsq(A, y, rcond = None)
w, b = paras


model_normal = LinearRegression()
model_outlier = LinearRegression()

X = x.reshape(-1, 1)

model_normal.fit(X, y)
model_outlier.fit(X, y_outlier)
print(w)
print(b)

print(model.coef_[0])
print(model.intercept_)

print(model_outlier.coef_[0])
print(model_outlier.intercept_)

y_pred_numpy = w * x + b
y_pred_sklearn = model.predict(x.reshape(-1, 1))

mse_numpy = np.mean((y - y_pred_numpy) ** 2)
mse_sklearn = np.mean((y - y_pred_sklearn) ** 2)

print("NumPy MSE:", mse_numpy)
print("sklearn MSE:", mse_sklearn)