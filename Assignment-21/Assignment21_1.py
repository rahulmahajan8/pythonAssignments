import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_thread(lst):
    print("Prime Numbers:")
    for i in lst:
        if is_prime(i):
            print(i, end=" ")
    print()

def nonprime_thread(lst):
    print("Non-Prime Numbers:")
    for i in lst:
        if not is_prime(i):
            print(i, end=" ")
    print()

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=prime_thread, args=(lst,))
t2 = threading.Thread(target=nonprime_thread, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()