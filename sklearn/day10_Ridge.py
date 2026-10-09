from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error


np.random.seed(42)
x = np.random.rand(100)*6-3
noise = np.random.randn(100)
y = 3*x + 2 +noise
X = x.reshape(-1,1)

X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("ridge", Ridge(alpha=1.0))
])

model.fit(X_train,y_train)
y_train_pred = model.predict(X_train)
y_val_pred = model.predict(X_val)


train_mse = mean_squared_error(y_train, y_train_pred)
val_mse = mean_squared_error(y_val, y_val_pred)

print(train_mse)
print(val_mse)