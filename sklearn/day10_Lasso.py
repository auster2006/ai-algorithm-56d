from sklearn.linear_model import Lasso
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
np.random.seed(42)

X = np.random.randn(100, 5)
noise = np.random.randn(100) * 0.3

y = 3 * X[:, 0] - 2 * X[:, 1] + noise

X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ("scaler",StandardScaler()),
    ("Lasso",Lasso(alpha=0.1,max_iter=10000))
])

model.fit(X_train,y_train)

print(model.named_steps["Lasso"].coef_)