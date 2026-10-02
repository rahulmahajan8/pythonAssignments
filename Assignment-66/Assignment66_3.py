import math

# Actual and predicted values
actual = [1, 0, 1, 1]
predicted = [0.9, 0.2, 0.8, 0.7]

# Mean Squared Error
def mean_squared_error(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        total += (a - p) ** 2

    return total / len(actual)


# Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    total = 0
    epsilon = 1e-10

    for a, p in zip(actual, predicted):
        p = max(min(p, 1 - epsilon), epsilon)
        total += -(a * math.log(p) + (1 - a) * math.log(1 - p))

    return total / len(actual)


# Calculate losses
mse = mean_squared_error(actual, predicted)
bce = binary_cross_entropy(actual, predicted)

# Display results
print("Actual Values   :", actual)
print("Predicted Values:", predicted)

print("\nMean Squared Error =", mse)
print("Binary Cross Entropy =", bce)

print("\nUse of Loss Functions:")
print("MSE is mainly used for regression problems.")
print("Binary Cross Entropy is mainly used for binary classification.")