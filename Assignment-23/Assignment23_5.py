import multiprocessing
import math
import os

def factorial(n):
    ans = math.factorial(n)

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Factorial :", ans)
    print()

if __name__ == "__main__":
    data = [10, 15, 20, 25]

    p = multiprocessing.Pool()
    p.map(factorial, data)

    p.close()
    p.join()