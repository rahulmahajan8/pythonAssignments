import threading

sum_result = 0
product_result = 1

def calculate_sum(lst):
    global sum_result
    sum_result = sum(lst)

def calculate_product(lst):
    global product_result
    product_result = 1
    for i in lst:
        product_result *= i

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=calculate_sum, args=(lst,))
t2 = threading.Thread(target=calculate_product, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum =", sum_result)
print("Product =", product_result)