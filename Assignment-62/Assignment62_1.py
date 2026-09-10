import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================================
# 1. Load Dataset
# ==========================================================

df = pd.read_csv("Employee_Attrition.csv")

print("========== EMPLOYEE ATTRITION DATASET ==========")

# ==========================================================
# 2. Display Shape, Columns and First Five Records
# ==========================================================

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst Five Records:")
print(df.head())

# ==========================================================
# 3. Check Missing Values
# ==========================================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================================
# 4. Identify Numerical and Categorical Features
# ==========================================================

numerical_features = df.select_dtypes(include=["int64", "float64"]).columns
categorical_features = df.select_dtypes(include=["object"]).columns

print("\nNumerical Features:")
print(list(numerical_features))

print("\nCategorical Features:")
print(list(categorical_features))

# ==========================================================
# 5. Convert OverTime into Numerical Representation
# ==========================================================

df["OverTime"] = df["OverTime"].map({
    "No": 0,
    "Yes": 1
})

# ==========================================================
# 6. Convert Attrition into 0 and 1
# ==========================================================

df["Attrition"] = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})

print("\nAfter Conversion:")
print(df.head())

# ==========================================================
# 7. Separate Independent and Dependent Variables
# ==========================================================

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

print("\nIndependent Variables:")
print(X.columns)

print("\nDependent Variable:")
print("Attrition")

# ==========================================================
# 8. Split Dataset into Training and Testing Data
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data :", X_test.shape)

# ==========================================================
# 9. Feature Scaling
# ==========================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==========================================================
# 10. Create MLP with Two Hidden Layers
# ==========================================================

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

# ==========================================================
# 11. Train the Network
# ==========================================================

model.fit(X_train, y_train)

print("\n========== MODEL TRAINING ==========")
print("Training completed successfully.")

# ==========================================================
# 12. Number of Iterations
# ==========================================================

print("\nNumber of Iterations:")
print(model.n_iter_)

# ==========================================================
# 13. Training Accuracy
# ==========================================================

train_pred = model.predict(X_train)

train_accuracy = accuracy_score(
    y_train,
    train_pred
)

print("\nTraining Accuracy:")
print(train_accuracy * 100, "%")

# ==========================================================
# 14. Testing Accuracy
# ==========================================================

test_pred = model.predict(X_test)

test_accuracy = accuracy_score(
    y_test,
    test_pred
)

print("\nTesting Accuracy:")
print(test_accuracy * 100, "%")

# ==========================================================
# 15. Confusion Matrix
# ==========================================================

cm = confusion_matrix(
    y_test,
    test_pred
)

print("\n========== CONFUSION MATRIX ==========")
print(cm)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        test_pred,
        target_names=["Stay", "Leave"]
    )
)

# ==========================================================
# 16. Plot Loss Curve
# ==========================================================

plt.figure(figsize=(8, 5))

plt.plot(
    model.loss_curve_
)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid()

plt.show()

# ==========================================================
# 17. Prediction Function
# ==========================================================

def PredictAttrition(employee_data):

    data = pd.DataFrame([employee_data])

    # Convert OverTime
    data["OverTime"] = data["OverTime"].map({
        "No": 0,
        "Yes": 1
    })

    # Scale data
    data_scaled = scaler.transform(data)

    # Predict
    prediction = model.predict(data_scaled)[0]

    probability = model.predict_proba(data_scaled)[0]

    print("\n========== PREDICTION ==========")

    if prediction == 0:
        print("Prediction: 0")
        print("Employee is likely to stay")
    else:
        print("Prediction: 1")
        print("Employee is likely to leave")

    print("Stay Probability :",
          round(probability[0] * 100, 2), "%")

    print("Leave Probability:",
          round(probability[1] * 100, 2), "%")

    return prediction


# ==========================================================
# 18. Test Using Five Employee Records
# ==========================================================

print("\n========== FIVE EMPLOYEE TEST RECORDS ==========")

employees = [
    {
        "Age": 24,
        "MonthlyIncome": 52421,
        "YearsAtCompany": 1,
        "TotalWorkingYears": 3,
        "DistanceFromHome": 10,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 1
    },

    {
        "Age": 51,
        "MonthlyIncome": 173064,
        "YearsAtCompany": 10,
        "TotalWorkingYears": 25,
        "DistanceFromHome": 5,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 4,
        "OverTime": "No",
        "NumCompaniesWorked": 1,
        "TrainingTimesLastYear": 3
    },

    {
        "Age": 47,
        "MonthlyIncome": 133296,
        "YearsAtCompany": 8,
        "TotalWorkingYears": 20,
        "DistanceFromHome": 7,
        "JobSatisfaction": 3,
        "WorkLifeBalance": 3,
        "OverTime": "No",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 2
    },

    {
        "Age": 38,
        "MonthlyIncome": 100482,
        "YearsAtCompany": 5,
        "TotalWorkingYears": 12,
        "DistanceFromHome": 15,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 3,
        "TrainingTimesLastYear": 2
    },

    {
        "Age": 38,
        "MonthlyIncome": 28122,
        "YearsAtCompany": 3,
        "TotalWorkingYears": 8,
        "DistanceFromHome": 20,
        "JobSatisfaction": 3,
        "WorkLifeBalance": 3,
        "OverTime": "No",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 1
    }
]

for i, employee in enumerate(employees, 1):

    print("\nEmployee", i)

    PredictAttrition(employee)


# ==========================================================
# 19. Check Overfitting / Underfitting
# ==========================================================

print("\n========== MODEL ANALYSIS ==========")

difference = train_accuracy - test_accuracy

print("Training Accuracy:",
      round(train_accuracy * 100, 2), "%")

print("Testing Accuracy:",
      round(test_accuracy * 100, 2), "%")

print("Difference:",
      round(difference * 100, 2), "%")

if train_accuracy > 0.95 and difference > 0.10:

    print("\nModel may be suffering from OVERFITTING.")

elif train_accuracy < 0.70 and test_accuracy < 0.70:

    print("\nModel may be suffering from UNDERFITTING.")

else:

    print("\nModel does not show strong signs of")
    print("overfitting or underfitting.")