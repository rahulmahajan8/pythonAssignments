import threading

def evenfactor(no):
    total = 0
    print("even factors:")
    for i in range(1,no +1):
        if no % i == 0 and i % 2 ==0:
            print(i,end=" ")
            total += i
    print("\n sum of even factors=",total)

def oddfactor(no):
    total = 0
    print("odd factors:")
    for i in range(1,no +1):
        if no % i == 0 and i % 2 != 0:
            print(i,end=" ")
            total += i
    print("\n sum of odd factors=",total)

num=int(input("Enter number:"))

t1= threading.Thread(target=evenfactor,args=(num,),name="evenfactor")
t2=threading.Thread(target=oddfactor,args=(num,),name="oddfactor")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit From Main")