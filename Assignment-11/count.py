num=int(input("enter a number:"))

count=0
while num>0:
    count +=1
    num=num // 10
print("count  of digit=",count)