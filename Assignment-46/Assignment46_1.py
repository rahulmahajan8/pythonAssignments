# Linear Regression - Advertising Dataset

# Step 1: Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the dataset
df = pd.read_csv("Advertising.csv")

print("Dataset:")
print(df)

# Step 3: Select input and output features

X = df[['TV', 'radio', 'newspaper']]


Y = df['sales']

# Step 4: Split the dataset into training and testing data

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

# Step 5: Create Linear Regression model
model = LinearRegression()

# Step 6: Train the model
model.fit(X_train, Y_train)

# Step 7: Test the model
Y_pred = model.predict(X_test)

# Step 8: Display predicted and expected values
print("\nPredicted Sales:")
print(Y_pred)

print("\nExpected Sales:")
print(Y_test.values)

# Step 9: Display model coefficients
print("\nModel Coefficients:")
print("TV coefficient       :", model.coef_[0])
print("Radio coefficient    :", model.coef_[1])
print("Newspaper coefficient:", model.coef_[2])
print("Intercept             :", model.intercept_)

# Step 10: Calculate performance
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)