import sys
import os
import time
import Helper

def CreateLog(dirname):

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filename = os.path.join(dirname,
            "ProcessLog_"+time.strftime("%Y%m%d_%H%M%S")+".log")

    fobj = open(filename,"w")

    data = Helper.GetProcessInfo()

    fobj.write("Running Process Information\n")
    fobj.write("="*60+"\n")

    for proc in data:
        fobj.write(f"PID : {proc['pid']}\n")
        fobj.write(f"Name : {proc['name']}\n")
        fobj.write(f"User : {proc['username']}\n")
        fobj.write("-"*40+"\n")

    fobj.close()

    print("Log created :",filename)

if __name__=="__main__":

    if len(sys.argv)!=2:
        print("Usage : ProcInfoLog.py DirectoryName")
        exit()

    CreateLog(sys.argv[1])