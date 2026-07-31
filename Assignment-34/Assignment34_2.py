import sys
import Helper

def Display(name):

    data = Helper.GetProcessInfo(name)

    if len(data)==0:
        print("Process not running")
        return

    for proc in data:
        print("PID :",proc['pid'])
        print("Name :",proc['name'])
        print("User :",proc['username'])
        print("-"*40)

if __name__=="__main__":

    if len(sys.argv)!=2:
        print("Usage : ProcInfo.py ProcessName")
        exit()

    Display(sys.argv[1])