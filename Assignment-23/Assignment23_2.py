import multiprocessing
import os

def sum_odd(n):
    count = (n + 1) // 2
    total = count * count

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Odd Numbers :", total)
    print()

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()
    p.map(sum_odd, data)

    p.close()
    p.join()