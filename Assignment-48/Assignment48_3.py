import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [20000, 25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)

# Input feature
X = df[["Experience"]]

# Target feature
Y = df["Salary"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Print coefficient and intercept
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict salary for 6 years
prediction = model.predict([[6]])

print("Predicted Salary for 6 Years Experience: ₹", prediction[0])

# Predict salary for all training data
Y_pred = model.predict(X)

# Plot data points
plt.scatter(X, Y, label="Data Points")

# Plot regression line
plt.plot(X, Y_pred, label="Regression Line")

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.legend()
plt.show()