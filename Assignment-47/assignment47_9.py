import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "SleepHours": [7, 6, 7, 6, 8],
    "Marks": [50, 55, 60, 65, 70]
}

df = pd.DataFrame(data)

# Input features
X = df[["StudyHours", "SleepHours"]]

# Target
Y = df["Marks"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Print coefficients
print("Coefficient of StudyHours:", model.coef_[0])
print("Coefficient of SleepHours:", model.coef_[1])

# Print intercept
print("Intercept:", model.intercept_)