numbers=[10,15,20,25,33,45,44,65,62,2,4]

Division=list(filter(lambda no: no % 3==0 and no % 5==0,numbers))
print("Divisible by 3 and 5:",Division)