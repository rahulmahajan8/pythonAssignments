import threading

def Thread1():
    print("Thread1 : Numbers from 1 to 50")
    for i in range(1, 51):
        print(i, end=" ")
    print("\nThread1 Completed")


def Thread2():
    print("Thread2 : Numbers from 50 to 1")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\nThread2 Completed")


t1 = threading.Thread(target=Thread1, name="Thread1")
t2 = threading.Thread(target=Thread2, name="Thread2")


t1.start()

t1.join()

t2.start()

t2.join()

print("\nAll threads completed.")