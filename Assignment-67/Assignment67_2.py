import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Dataset
X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

# Output
# 0 = Loan Rejected
# 1 = Loan Approved
y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

# Feature names
print("Features:")
print("1. Applicant Income")
print("2. Credit Score")
print("3. Loan Amount")
print("4. Existing EMI")
print("5. Employment Status")

# Preprocess categorical value
# Employment Status:
# 0 = Not Stable
# 1 = Stable
print("\nEmployment status is already encoded as 0 and 1.")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Apply scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create FNN model
model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation='relu',
    solver='lbfgs',
    max_iter=5000,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nActual Test Values    :", y_test)
print("Predicted Test Values :", y_pred)
print("Model Accuracy        :", accuracy * 100, "%")

# New applicant
new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

# Scale new applicant
new_applicant_scaled = scaler.transform(new_applicant)

# Predict loan approval
prediction = model.predict(new_applicant_scaled)

# Display result
print("\nNew Applicant:")
print("Income           = 55000")
print("Credit Score     = 720")
print("Loan Amount      = 400000")
print("Existing EMI     = 10000")
print("Employment       = Stable")

if prediction[0] == 1:
    print("\nPrediction: Loan Approved")
else:
    print("\nPrediction: Loan Rejected")