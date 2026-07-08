def chknum(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

num=int(input("Enter a number:"))

chknum(num)