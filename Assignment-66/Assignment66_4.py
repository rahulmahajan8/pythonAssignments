# Take input values
x = float(input("Enter input: "))
weight = float(input("Enter weight: "))
bias = float(input("Enter bias: "))
target = float(input("Enter target output: "))
learning_rate = float(input("Enter learning rate: "))

# Calculate prediction
prediction = (x * weight) + bias

# Calculate error
error = target - prediction

# Store old weight
old_weight = weight

# Update weight using gradient descent
weight = weight + learning_rate * error * x

# Display results
print("\nPrediction =", prediction)
print("Error =", error)
print("Old Weight =", old_weight)
print("Updated Weight =", weight)