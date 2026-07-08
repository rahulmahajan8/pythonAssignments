def maximum(arr):
    max_num = arr[0]

    for i in arr:
        if i > max_num:
            max_num = i
    return max_num
    

n = int(input("Enter a Number of Elements:"))

data=[]
for i in range(n):
    value = int(input())
    data.append(value)

print("maximum number is:",maximum(data))