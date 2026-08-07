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

# =====================================================
# Question 2
# Remove SleepHours
# =====================================================

print("\nQuestion 2")

X2 = df.drop(["SleepHours", "FinalResult"], axis=1)

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X2,
    y,
    test_size=0.2,
    random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train2, y_train2)

pred2 = model2.predict(X_test2)

acc2 = accuracy_score(y_test2, pred2)

print("Old Accuracy =", accuracy)
print("New Accuracy =", acc2)

# =====================================================
# Question 3
# Use only StudyHours and Attendance
# =====================================================

print("\nQuestion 3")

X3 = df[["StudyHours", "Attendance"]]

X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X3,
    y,
    test_size=0.2,
    random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X_train3, y_train3)

pred3 = model3.predict(X_test3)

acc3 = accuracy_score(y_test3, pred3)

print("Accuracy =", acc3)

# =====================================================
# Question 4
# Predict 5 New Students
# =====================================================

print("\nQuestion 4")

new_students = pd.DataFrame({
    "StudyHours":[5,2,7,8,3],
    "Attendance":[90,60,95,85,70],
    "PreviousScore":[80,50,88,91,65],
    "AssignmentsCompleted":[9,4,10,8,5],
    "SleepHours":[7,6,8,7,5]
})

prediction = model.predict(new_students)

new_students["Prediction"] = prediction

new_students["Prediction"] = new_students["Prediction"].map({
    1:"Pass",
    0:"Fail"
})

print(new_students)

# =====================================================
# Question 5
# Manual Accuracy
# =====================================================

print("\nQuestion 5")

correct = (y_test.values == y_pred).sum()

manual_accuracy = correct / len(y_test)

print("Manual Accuracy =", manual_accuracy)
print("Sklearn Accuracy =", accuracy)

# =====================================================
# Question 6
# Misclassified Students
# =====================================================

print("\nQuestion 6")

misclassified = X_test.copy()

misclassified["Actual"] = y_test.values
misclassified["Predicted"] = y_pred

misclassified = misclassified[
    misclassified["Actual"] != misclassified["Predicted"]
]

print(misclassified)

print("Total Misclassified =", len(misclassified))

# =====================================================
# Question 7
# Different Random States
# =====================================================

print("\nQuestion 7")

for rs in [0,10,42]:

    X_train7, X_test7, y_train7, y_test7 = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=rs
    )

    model7 = DecisionTreeClassifier(random_state=rs)

    model7.fit(X_train7,y_train7)

    pred7 = model7.predict(X_test7)

    acc7 = accuracy_score(y_test7,pred7)

    print("Random State =", rs,
          " Accuracy =", acc7)