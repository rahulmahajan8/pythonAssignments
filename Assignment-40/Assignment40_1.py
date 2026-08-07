import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("student_performance_ml.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Information")
print(df.info())

# -------------------------------
# Prepare Data
# -------------------------------
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Train Decision Tree
# -------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy =", accuracy)

# =====================================================
# Question 1
# Feature Importance
# =====================================================

print("\nQuestion 1")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(importance)

print("\nMost Important Feature:")
print(importance.loc[importance["Importance"].idxmax()])

print("\nLeast Important Feature:")
print(importance.loc[importance["Importance"].idxmin()])