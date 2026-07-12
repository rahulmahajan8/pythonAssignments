from multiprocessing import Pool
import math
import os

def factorial(n):
    return(os.getpid(),n,math.factorial(n))

if __name__ == "__main__":
    numbers=[10,15,20,25]

    with Pool() as p:
        result = p.map(factorial,numbers)

        for pid,num,fact in result:
            print("process id:",pid)
            print("input number:",num)
            print("factorial:",fact)
            print()

