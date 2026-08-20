# Simple Linear Regression Manually

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# Calculate mean
x_mean = sum(X) / len(X)
y_mean = sum(Y) / len(Y)

# Calculate slope
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2

m = numerator / denominator

# Calculate intercept
c = y_mean - (m * x_mean)

# Predict Y for X = 6
x = 6
prediction = m * x + c

print("Mean of X =", x_mean)
print("Mean of Y =", y_mean)
print("Slope (m) =", m)
print("Intercept (c) =", c)

print("Regression Equation:")
print("Y =", m, "* X +", c)

print("Predicted Y for X = 6:", prediction)