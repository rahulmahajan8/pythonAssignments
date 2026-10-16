# Input Feature Map
feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

# Apply ReLU
relu_output = []

for row in feature_map:
    new_row = []
    for value in row:
        new_row.append(max(0, value))
    relu_output.append(new_row)

print("ReLU Output:")
for row in relu_output:
    print(row)

# Apply 2x2 Max Pooling with stride 1
max_value = max(
    relu_output[0][0], relu_output[0][1],
    relu_output[1][0], relu_output[1][1]
)

print("Max Pooling Output:")
print([[max_value]])