def sumdigit(n):
    count=0
    while n > 0:
        digit = n % 10
        count += digit
        n //= 10

    return count

num=int(input("Enter A Number:"))
print("Addition Of Digits",sumdigit(num))

    