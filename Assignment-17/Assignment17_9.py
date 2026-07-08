def countdigit(n):
    count=0
    while n > 0:
        count += 1
        n //= 10

    return count

num=int(input("Enter A Number:"))
print("Number Of Digits",countdigit(num))

    