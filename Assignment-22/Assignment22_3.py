from multiprocessing import Pool
import math

def countprime(n):
    count=0

    for num in range(2,n+1):
        prime=True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime= False
                break
        
        if prime:
            count += 1

    return ( n, count)

if __name__ == "__main__":
    numbers = [10000,20000,30000,40000]

    with Pool() as p:
        result = p.map(countprime,numbers)

    for n,cnt in result:
        print("prime count between 1 and",n,"=",cnt)
        