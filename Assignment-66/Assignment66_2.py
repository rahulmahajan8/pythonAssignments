import numpy as np
import matplotlib.pyplot as plt

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# Accept input value
x_input = float(input("Enter a value between -10 and 10: "))

if x_input < -10 or x_input > 10:
    print("Please enter a value between -10 and 10.")
else:
    print("Sigmoid =", sigmoid(x_input))
    print("ReLU =", relu(x_input))
    print("Tanh =", tanh(x_input))

# Values for plotting
x = np.linspace(-10, 10, 100)

# Calculate outputs
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# Plot Sigmoid
plt.plot(x, y_sigmoid)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Plot ReLU
plt.plot(x, y_relu)
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Plot Tanh
plt.plot(x, y_tanh)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Explanation
print("\nUses of Activation Functions:")
print("1. Sigmoid: Used mainly for binary classification.")
print("2. ReLU: Commonly used in hidden layers of neural networks.")
print("3. Tanh: Used when output values between -1 and 1 are required.")