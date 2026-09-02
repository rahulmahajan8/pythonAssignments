import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------

df = pd.read_csv("Customer_Loan_Approval.csv")

print("First 5 records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# ---------------------------------------------------------
# 2. Check for missing values
# ---------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows containing missing values
df = df.dropna()

# ---------------------------------------------------------
# 3. Separate input and output variables
# ---------------------------------------------------------

X = df.drop("LoanApproved", axis=1)
y = df["LoanApproved"]

print("\nInput Variables:")
print(X.columns)

print("\nOutput Variable:")
print("LoanApproved")

# ---------------------------------------------------------
# 4. Split dataset into training and testing data
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data :", X_test.shape)

# ---------------------------------------------------------
# Scaling data for Logistic Regression and KNN
# ---------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------------------------------------
# 5. Train Logistic Regression
# ---------------------------------------------------------

logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train_scaled, y_train)

logistic_pred = logistic_model.predict(X_test_scaled)

logistic_accuracy = accuracy_score(y_test, logistic_pred)

print("\nLogistic Regression Accuracy:",
      logistic_accuracy * 100, "%")

# ---------------------------------------------------------
# 6. Train Decision Tree
# ---------------------------------------------------------

decision_tree = DecisionTreeClassifier(
    random_state=42
)

decision_tree.fit(X_train, y_train)

decision_pred = decision_tree.predict(X_test)

decision_accuracy = accuracy_score(
    y_test,
    decision_pred
)

print("Decision Tree Accuracy:",
      decision_accuracy * 100, "%")

# ---------------------------------------------------------
# 7. Train KNN
# ---------------------------------------------------------

knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train_scaled, y_train)

knn_pred = knn_model.predict(X_test_scaled)

knn_accuracy = accuracy_score(
    y_test,
    knn_pred
)

print("KNN Accuracy:",
      knn_accuracy * 100, "%")

# ---------------------------------------------------------
# 8. Hard Voting Classifier
# ---------------------------------------------------------

hard_voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="hard"
)

# Hard voting uses the original input data.
# KNN and Logistic Regression work better with scaled data,
# so for a simple assignment implementation we use the
# standardized data for all three models.

hard_voting.fit(X_train_scaled, y_train)

hard_pred = hard_voting.predict(X_test_scaled)

hard_accuracy = accuracy_score(
    y_test,
    hard_pred
)

print("Hard Voting Accuracy:",
      hard_accuracy * 100, "%")

# ---------------------------------------------------------
# 9. Soft Voting Classifier
# ---------------------------------------------------------

soft_voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="soft"
)

soft_voting.fit(X_train_scaled, y_train)

soft_pred = soft_voting.predict(X_test_scaled)

soft_accuracy = accuracy_score(
    y_test,
    soft_pred
)

print("Soft Voting Accuracy:",
      soft_accuracy * 100, "%")

# ---------------------------------------------------------
# 10. Display comparison
# ---------------------------------------------------------

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],
    "Accuracy": [
        logistic_accuracy * 100,
        decision_accuracy * 100,
        knn_accuracy * 100,
        hard_accuracy * 100,
        soft_accuracy * 100
    ]
})

print("\n==========================================")
print("       MODEL ACCURACY COMPARISON")
print("==========================================")

print(results.to_string(index=False))

# ---------------------------------------------------------
# 11. Find the best model
# ---------------------------------------------------------

best_model = results.loc[
    results["Accuracy"].idxmax()
]

print("\n==========================================")
print("Best Model:", best_model["Model"])
print("Accuracy:", round(best_model["Accuracy"], 2), "%")
print("==========================================")