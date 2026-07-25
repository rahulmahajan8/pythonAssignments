import schedule
import time
import os
from datetime import datetime

directory = input("demo.txt: ")

def ScanDirectory():
    if not os.path.exists(directory):
        print("Directory not found.")
        return

    files = 0
    folders = 0

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            files += 1
        elif os.path.isdir(path):
            folders += 1

    print("Directory Scanned:", directory)
    print("Total Files:", files)
    print("Total Subdirectories:", folders)
    print("Scan Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print()

schedule.every(1).minutes.do(ScanDirectory)

while True:
    schedule.run_pending()
    time.sleep(1)