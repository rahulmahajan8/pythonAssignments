def minimum(arr):
    min_num = arr[0]

    for i in arr:
        if i < min_num:
            min_num = i
    return min_num
    

n = int(input("Enter a Number of Elements:"))

data=[]
for i in range(n):
    value = int(input())
    data.append(value)

print("minimum number is:",minimum(data))