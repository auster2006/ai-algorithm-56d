from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=3000,
    n_features=10,
    n_informative=5,
    n_redundant=0,
    weights=[0.95, 0.05],
    flip_y=0,
    random_state=42
)

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.4,
    stratify=y,
    random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    stratify=y_temp,
    random_state=42
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score
)

# 1. 训练普通逻辑回归
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 2. 在验证集上预测
y_pred = model.predict(X_val)
y_prob = model.predict_proba(X_val)[:, 1]

# 3. 计算评估指标
accuracy = accuracy_score(y_val, y_pred)
precision = precision_score(y_val, y_pred, zero_division=0)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)
roc_auc = roc_auc_score(y_val, y_prob)
ap = average_precision_score(y_val, y_prob)

# 4. 输出结果
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1:        {f1:.4f}")
print(f"ROC-AUC:   {roc_auc:.4f}")
print(f"AP:        {ap:.4f}")

model_balanced = LogisticRegression(
    class_weight="balanced",
    max_iter=1000
)

model_balanced.fit(X_train, y_train)

y_pred_balanced = model_balanced.predict(X_val)
y_prob_balanced = model_balanced.predict_proba(X_val)[:, 1]

print("Balanced Model:")
print("Accuracy:", accuracy_score(y_val, y_pred_balanced))
print("Precision:", precision_score(y_val, y_pred_balanced, zero_division=0))
print("Recall:", recall_score(y_val, y_pred_balanced))
print("F1:", f1_score(y_val, y_pred_balanced))
print("ROC-AUC:", roc_auc_score(y_val, y_prob_balanced))
print("AP:", average_precision_score(y_val, y_prob_balanced))

for threshold in [0.5, 0.4, 0.3, 0.2, 0.1]:
    y_pred_new = (y_prob >= threshold).astype(int)

    precision = precision_score(y_val, y_pred_new, zero_division=0)
    recall = recall_score(y_val, y_pred_new)
    f1 = f1_score(y_val, y_pred_new)

    print(
        f"Threshold={threshold:.1f} | "
        f"Precision={precision:.4f} | "
        f"Recall={recall:.4f} | "
        f"F1={f1:.4f}"
    )