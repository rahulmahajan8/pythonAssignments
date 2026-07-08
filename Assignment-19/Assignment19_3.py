from functools import reduce
data=list(map(int , input("Enter number:").split()))

filterdata=list(filter(lambda x:x>=70 and x<=90,data))
print("List after filter=",filterdata)

mapdata=list(map(lambda x:x+10,filterdata))
print("List after map=",mapdata)

result=reduce(lambda x,y:x * y,mapdata)
print("output of reduce=",result)