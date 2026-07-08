import threading

def evenlist(lst):
    even=[i for i in lst if i % 2 == 0]
    print("even elements:",even)
    print("sum of even elements:",sum(even))

def oddlist(lst):
    odd=[i for i in lst if i % 2 != 0]
    print("odd elements:",odd)
    print("sum of odd elements:",sum(odd))

lst=list(map(int,input("enter list elements:").split()))

t1= threading.Thread(target=evenlist,args=(lst,),name="evenlist")
t2=threading.Thread(target=oddlist,args=(lst,),name="oddlist")

t1.start()
t2.start()

t1.join()
t2.join()
