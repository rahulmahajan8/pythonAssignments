# ==========================================================
# Decision Tree Classifier - Student Performance Prediction
# ==========================================================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ==========================================================
# Step 2: Load Dataset
# ==========================================================

data = pd.read_csv("student_performance_ml.csv")

print("First 5 Records:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

# ==========================================================
# Step 3: Data Analysis
# ==========================================================

print("\nStatistical Summary:")
print(data.describe())

print("\nClass Distribution:")
print(data["FinalResult"].value_counts())

# ==========================================================
# Step 4: Visualization
# ==========================================================

plt.figure(figsize=(6,4))
data["FinalResult"].value_counts().plot(kind="bar", color=["red","green"])
plt.title("Pass and Fail Count")
plt.xlabel("Final Result")
plt.ylabel("Students")
plt.show()

# ==========================================================
# Step 5: Train-Test Split
# ==========================================================

X = data[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

y = data["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================================
# Step 6: Model Training
# ==========================================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# ==========================================================
# Step 7: Prediction
# ==========================================================

y_pred = model.predict(X_test)

print("\nActual Values")
print(y_test.values)

print("\nPredicted Values")
print(y_pred)

print("\nActual vs Predicted")

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print(result)

# ==========================================================
# Step 8: Accuracy Calculation
# ==========================================================

accuracy = accuracy_score(y_test, y_pred)

print("\nTesting Accuracy = {:.2f}%".format(accuracy * 100))

# ==========================================================
# Step 9: Confusion Matrix
# ==========================================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

# ==========================================================
# True Positive, True Negative, False Positive, False Negative
# ==========================================================

TN, FP, FN, TP = cm.ravel()

print("\nTrue Positive :", TP)
print("True Negative :", TN)
print("False Positive:", FP)
print("False Negative:", FN)

# ==========================================================
# Training Accuracy
# ==========================================================

train_pred = model.predict(X_train)

train_accuracy = accuracy_score(y_train, train_pred)

print("\nTraining Accuracy = {:.2f}%".format(train_accuracy * 100))

# ==========================================================
# Compare Training and Testing Accuracy
# ==========================================================

print("\nComparison")

print("Training Accuracy :", round(train_accuracy * 100, 2), "%")
print("Testing Accuracy  :", round(accuracy * 100, 2), "%")

if train_accuracy > accuracy + 0.10:
    print("Model is Overfitting.")
elif accuracy > train_accuracy:
    print("Model is Underfitting.")
else:
    print("Model is Well Balanced.")

# ==========================================================
# Train Three Decision Tree Models
# ==========================================================

depths = [1, 3, None]

print("\nTesting Accuracy for Different max_depth Values")

for d in depths:

    clf = DecisionTreeClassifier(max_depth=d, random_state=42)

    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)

    acc = accuracy_score(y_test, pred)

    print("max_depth =", d, "-->", round(acc * 100, 2), "%")

# ==========================================================
# Predict New Student
# ==========================================================

new_student = [[
    6,      # StudyHours
    85,     # Attendance
    66,     # PreviousScore
    7,      # AssignmentsCompleted
    7       # SleepHours
]]

prediction = model.predict(new_student)

print("\nPrediction for New Student")

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

# ==========================================================
# Final Conclusion
# ==========================================================

print("\nProgram Completed Successfully.")