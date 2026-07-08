import marvellousNum

def Listprime(arr):
    total=0

    for i in arr:
        if marvellousNum.chkprime(i):
            toal += i
    return total

n=int(input("Enter element to elements:"))

data=[]

for i in range(n):
    value=int(input())
    data.append(value)


print("Addition of prime number is:",Listprime(data))