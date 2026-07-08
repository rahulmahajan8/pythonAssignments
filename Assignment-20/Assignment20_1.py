import threading

def even():
    print("first 10 even numbers:")
    for i in range(2,21,2):
        print(i,end=" ")
    print()

def odd():
    print("first 10 odd numbers:")
    for i in range(1,20,2):
        print(i, end=" ")
    print()

t1= threading.Thread(target=even,name="even")
t2=threading.Thread(target=odd,name="odd")

t1.start()
t2.start()

t1.join()
t2.join()