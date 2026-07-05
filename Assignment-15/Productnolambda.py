from functools import reduce
numbers=[10,15,20,25,33,45,44,65,62,2,4]

product=reduce(lambda x,y: x*y,numbers)
print("product is:",product)
