from functools import reduce

def isprime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
        return True

data=list(map(int , input("Enter NUmbers:").split()))

filterdata=list(filter(isprime,data))
print("list after filter=",filterdata)

mapdata=list(map(lambda x: x * 2,filterdata))
print("List after map=",mapdata)

result=reduce(lambda x,y : x if x > y else y,mapdata)
print("Output of reduce=",result)