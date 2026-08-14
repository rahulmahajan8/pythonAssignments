import math

data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

distances = []

for hours, attend, result in data:
    distance = math.sqrt(
        (study_hours - hours) ** 2 +
        (attendance - attend) ** 2
    )

    distances.append((distance, result))

distances.sort()

k = 3
nearest = distances[:k]

pass_count = 0
fail_count = 0

for distance, result in nearest:
    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

if pass_count > fail_count:
    prediction = "Pass"
else:
    prediction = "Fail"

print("\nPredicted Result:", prediction)