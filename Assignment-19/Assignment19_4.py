from functools import reduce

data=list(map(int , input("Enter NUmbers:").split()))

filterdata=list(filter(lambda x: x % 2 == 0,data))
print("list after filter=",filterdata)

mapdata=list(map(lambda x: x * x,filterdata))
print("List after map=",mapdata)

result=reduce(lambda x,y : x + y,mapdata)
print("Output of reduce=",result)