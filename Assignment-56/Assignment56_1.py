# ============================================================
# Fraudulent Transaction Detection using Ensemble Learning
# ============================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# ============================================================
# 2. CHECK FOR MISSING VALUES
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows having missing values
df = df.dropna()


# ============================================================
# 3. SEPARATE INPUT AND OUTPUT
# ============================================================

# Target column
X = df.drop("Fraud", axis=1)
y = df["Fraud"]


# If DeviceType is categorical, convert it into numerical
X = pd.get_dummies(X, drop_first=True)

print("\nInput Features:")
print(X.columns)

print("\nTarget:")
print("Fraud")


# ============================================================
# 4. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data :", X_test.shape)


# ============================================================
# 5. CREATE MODELS
# ============================================================

# ------------------------------------------------------------
# Decision Tree
# ------------------------------------------------------------

decision_tree = DecisionTreeClassifier(
    random_state=42
)


# ------------------------------------------------------------
# Bagging Classifier
# ------------------------------------------------------------

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=50,
    random_state=42
)


# ------------------------------------------------------------
# Random Forest
# ------------------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ------------------------------------------------------------
# AdaBoost
# ------------------------------------------------------------

adaboost = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(
        max_depth=1,
        random_state=42
    ),
    n_estimators=50,
    random_state=42
)


# ------------------------------------------------------------
# Voting Classifier
# ------------------------------------------------------------

voting = VotingClassifier(
    estimators=[
        ("decision_tree",
         DecisionTreeClassifier(random_state=42)),

        ("random_forest",
         RandomForestClassifier(
             n_estimators=100,
             random_state=42
         )),

        ("logistic_regression",
         LogisticRegression(max_iter=1000))
    ],
    voting="hard"
)


# ============================================================
# 6. TRAIN ALL MODELS
# ============================================================

models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": random_forest,
    "AdaBoost": adaboost,
    "Voting": voting
}


results = []


for name, model in models.items():

    print("\n========================================")
    print("Training:", name)
    print("========================================")

    # Train
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )
    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )
    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    # Print results
    print("Accuracy :", round(accuracy * 100, 2), "%")
    print("Precision:", round(precision * 100, 2), "%")
    print("Recall   :", round(recall * 100, 2), "%")
    print("F1 Score :", round(f1 * 100, 2), "%")

    print("\nConfusion Matrix:")
    print(cm)

    # Store results
    results.append([
        name,
        accuracy * 100,
        precision * 100,
        recall * 100,
        f1 * 100
    ])


# ============================================================
# 7. FINAL COMPARISON
# ============================================================

comparison = pd.DataFrame(
    results,
    columns=[
        "Algorithm",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)


print("\n\n==========================================================")
print("              FINAL MODEL COMPARISON")
print("==========================================================")

print(
    comparison.to_string(
        index=False,
        formatters={
            "Accuracy": "{:.2f}".format,
            "Precision": "{:.2f}".format,
            "Recall": "{:.2f}".format,
            "F1": "{:.2f}".format
        }
    )
)


# ============================================================
# 8. FIND BEST MODEL
# ============================================================

best_model = comparison.loc[
    comparison["F1"].idxmax()
]

print("\n==========================================================")
print("                  BEST MODEL")
print("==========================================================")

print("Algorithm :", best_model["Algorithm"])
print("Accuracy  :", round(best_model["Accuracy"], 2), "%")
print("Precision :", round(best_model["Precision"], 2), "%")
print("Recall    :", round(best_model["Recall"], 2), "%")
print("F1 Score  :", round(best_model["F1"], 2), "%")

print("\nRecommendation:")
print(
    "The model with the highest F1 Score is recommended "
    "for fraudulent transaction detection."
)

print("==========================================================")