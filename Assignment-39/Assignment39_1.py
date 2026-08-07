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
