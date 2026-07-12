from multiprocessing import Pool

def sumofsquare(n):
    return sum(i*i for i in range(1,n+1))

if __name__ == "__main__":
    numbers=[1000000,2000000,3000000,4000000]

    with Pool() as p :
        result = p.map(sumofsquare,numbers)

    print(result)
