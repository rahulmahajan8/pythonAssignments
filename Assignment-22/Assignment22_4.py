from multiprocessing import Pool
import time

def sum_of_fifth_powers(n):
    return sum(i ** 5 for i in range(1, n + 1))

if __name__ == "__main__":
    numbers = [1000000, 2000000, 30000000, 4000000]

    start = time.time()

    with Pool() as p:
        result = p.map(sum_of_fifth_powers, numbers)

    end = time.time()

    print(result)
    print("Execution Time:", end - start, "seconds")