# Model Performance

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# Regression equation
m = 0.4
c = 2.4

# Predict all Y values
predicted = []

for x in X:
    y_pred = m * x + c
    predicted.append(y_pred)

print("Actual Y values:", Y)
print("Predicted Y values:", predicted)

# Calculate MSE
squared_error = []

for i in range(len(Y)):
    error = Y[i] - predicted[i]
    squared_error.append(error ** 2)

mse = sum(squared_error) / len(Y)

# Calculate R2
y_mean = sum(Y) / len(Y)

sst = 0
for y in Y:
    sst += (y - y_mean) ** 2

sse = sum(squared_error)

r2 = 1 - (sse / sst)

print("\nSquared Errors:", squared_error)
print("MSE =", mse)
print("R2 Score =", r2)