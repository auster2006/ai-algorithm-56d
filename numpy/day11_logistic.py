import numpy as np
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression

X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)


def sigmoid(z):
    # 你来实现
    return 1/(1+np.exp(-z))

def binary_cross_entropy(y, p):
    p = np.clip(p, 1e-12, 1 - 1e-12)

    # 根据 BCE 公式计算平均损失
    loss = -np.mean(y*np.log(p)+(1-y)*np.log(1-p))

    return loss

def train_logistic_regression(X, y, lr=0.1, epochs=1000):
    n, d = X.shape

    w = np.zeros(d)
    b = 0.0

    for epoch in range(epochs):

        # 1. 计算线性输出
        z = X @ w + b

        # 2. 计算预测概率
        p = sigmoid(z)

        # 3. 计算梯度
        dw = X.T @ (p-y)/n
        db = np.mean(p-y)

        # 4. 更新参数
        w = w - dw*lr
        b = b - db*lr

    return w, b


w, b = train_logistic_regression(X_train, y_train, lr=0.1, epochs=1000)

p = sigmoid(X_val @ w + b)

y_pred = (p >= 0.5).astype(int)

print((p >= 0.5).astype(int))

print(np.mean(y_pred == y_val))

print("Accuracy:", accuracy_score(y_val, y_pred))
print("F1:", f1_score(y_val, y_pred))
print("AUC:", roc_auc_score(y_val, p))

model = LogisticRegression(
    C=1e6,
    max_iter=1000
)

model.fit(X_train, y_train)

sklearn_pred = model.predict(X_val)
sklearn_proba = model.predict_proba(X_val)[:, 1]

print("Accuracy2:", accuracy_score(y_val, sklearn_pred))
print("F12:", f1_score(y_val, sklearn_pred))
print("AUC2:", roc_auc_score(y_val, p))