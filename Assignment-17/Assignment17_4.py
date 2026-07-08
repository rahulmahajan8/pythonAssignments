def sumfactorial(n):
    total = 0
    for i in range(1,n):
       if n % i == 0:
           total += i
    return total

num=int(input("Enter number:"))
print("addition of Factorial=",sumfactorial(num))