# Input Image Matrix
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Kernel Matrix
kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

# Perform Convolution
feature_map = []

for i in range(3):
    row = []
    for j in range(3):
        total = 0
        for ki in range(3):
            for kj in range(3):
                total += image[i + ki][j + kj] * kernel[ki][kj]
        row.append(total)
    feature_map.append(row)

print("Feature Map:")
for row in feature_map:
    print(row)