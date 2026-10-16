# Input 2D Matrix
matrix = [
    [6, 4],
    [8, 6]
]

# Convert 2D Matrix into 1D Vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Flatten Output:", flatten_output)

# Fully Connected Layer
weights = [1, 2, 1, 2]
bias = 0

output = 0
for i in range(len(flatten_output)):
    output += flatten_output[i] * weights[i]

output += bias

print("Final Output:", output)