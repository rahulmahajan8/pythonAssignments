from functools import reduce
numbers=[10,15,20,25,33,45,44,65,62]
addition=reduce (lambda x,y:x+y,numbers)
print("Addition:",addition)
