import multiprocessing
import os

def sum_even(n):
    total = (n // 2) * ((n // 2) + 1)
    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Even Numbers :", total)
    print()

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    p.map(sum_even, data)

    p.close()
    p.join()