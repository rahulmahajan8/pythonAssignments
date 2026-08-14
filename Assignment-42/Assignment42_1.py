import math

data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# Take input from user
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

for point, px, py, label in data:
    distance = math.sqrt((x - px) ** 2 + (y - py) ** 2)
    distances.append((distance, point, label))

distances.sort()

# K = 3
k = 3


nearest = distances[:k]

print("\nNearest Neighbors:")

for distance, point, label in nearest:
    print(f"{point} - Distance: {distance:.2f}")

red_count = 0
blue_count = 0

for distance, point, label in nearest:
    if label == "Red":
        red_count += 1
    else:
        blue_count += 1

# Prediction
if red_count > blue_count:
    prediction = "Red"
else:
    prediction = "Blue"

print("\nPredicted Class:", prediction)