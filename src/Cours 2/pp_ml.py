import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flake8.style_guide import Decision
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, plot_tree

train_data = pd.read_csv("data/fraud_train.csv")
test_data = pd.read_csv("data/fraud_test.csv")

X_train = train_data.drop("is_fraud", axis=1)
y_train = train_data["is_fraud"]

X_test = test_data.drop("is_fraud", axis=1)
y_test = test_data["is_fraud"]

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(50, 50))
plot_tree(
    model,
    feature_names=X_train.columns,
    class_names=["Not Fraud", "Fraud"],
    filled=True,
    rounded=True,
)
plt.title("Decision Tree Dami marche moi dessus")
plt.show()

confusion_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Reds")
plt.title("Confusion Matrix Sua tu es ma Queen")
plt.ylabel("True Label")
plt.xlabel("Predicted")
plt.show()
