from functools import reduce
numbers=[10,15,20,25,33,45,44,65,62,2,4]

Minimum= reduce(lambda x,y: x if x<y else y,numbers)
print("Minimun num:",Minimum)