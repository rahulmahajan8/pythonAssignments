import multiprocessing
import os

def count_even(n):
    total = n // 2

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Even Number Count :", total)
    print()

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    p.map(count_even, data)

    p.close()
    p.join()