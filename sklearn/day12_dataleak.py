from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
import numpy as np


X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=0,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

Accuracy = accuracy_score(y_pred,y_test)

auc = roc_auc_score(y_test,y_prob)
print("Accuracy:", Accuracy)
print("ROC-AUC:", auc)


X_train_leak = np.column_stack([X_train, y_train])
X_test_leak = np.column_stack([X_test, y_test])

model2 = LogisticRegression()

model2.fit(X_train_leak,y_train)

y_pred2 = model2.predict(X_test_leak)
y_prob2 = model2.predict_proba(X_test_leak)[:, 1]

Accuracy2 = accuracy_score(y_pred2,y_test)

auc2 = roc_auc_score(y_test,y_prob2)

print("Accuracy:", Accuracy2)
print("ROC-AUC:", auc2)