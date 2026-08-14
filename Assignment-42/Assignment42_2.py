import math

data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# New point
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

for point, px, py, label in data:
    distance = math.sqrt((x - px) ** 2 + (y - py) ** 2)
    distances.append((distance, point, label))

distances.sort()

def predict(k):
    if k > len(data):
        return "Invalid K"

    nearest = distances[:k]

    red = 0
    blue = 0

    for distance, point, label in nearest:
        if label == "Red":
            red += 1
        else:
            blue += 1

    if red > blue:
        return "Red"
    else:
        return "Blue"


print("\nPrediction Results")

print("K = 1 ->", predict(1))
print("K = 3 ->", predict(3))
print("K = 5 ->", predict(5))