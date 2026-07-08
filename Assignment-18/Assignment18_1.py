def listsum(arr):
    total = 0
    for i in arr:
        total += i
    return total

n = int(input("Enter a Number of Elements:"))

data=[]
for i in range(n):
    value = int(input())
    data.append(value)

print("addition is:",listsum(data))