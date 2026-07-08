def pattern(n):

    for i in range(n):
        for j in range(1,n+1):
            print(j,end= " ")
        print()

num=int(input("Enter A Number:"))

pattern(num)
