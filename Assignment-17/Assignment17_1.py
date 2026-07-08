import Arithmetic

def main():
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))

    print("Addition=",Arithmetic.add(b))
    print("Substraction=",Arithmetic.sub(a,b))
    print("Multiplication=",Arithmetic.mul(a,b))
    print("Division=",Arithmetic.div(a,b))

if __name__ == "main":
    main()