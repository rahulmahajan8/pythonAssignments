def frequency(arr,no):
    count=0

    for i in arr:
        if i == no:
            count += 1
    return count

n=int(input("Enter element to search"))

data=[]

for i in range(n):
    value=int
    data.append(value)

num=int(input("Enter element to search:"))

print("Frequency is:",frequency(data,num))