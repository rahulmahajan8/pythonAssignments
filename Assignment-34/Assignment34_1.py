import Helper

def Display():
    data = Helper.GetProcessInfo()

    for proc in data:
        print("PID :",proc['pid'])
        print("Name :",proc['name'])
        print("User :",proc['username'])
        print("-"*40)

if __name__=="__main__":
    Display()