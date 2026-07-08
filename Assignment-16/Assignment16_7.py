def Division(no):

    if no % 5 == 0:
        return True
    else:
        return False
    
num=int(input("Enter a number:"))

print(Division(num))