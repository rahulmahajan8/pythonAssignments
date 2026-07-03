def checkgreater(a,b):
    if a > b:
        print(a,"is greater")
    elif b > a:
        print(b,"is greater")
    else:
        print("both number are equal")

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

checkgreater(num1,num2)