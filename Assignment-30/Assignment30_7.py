import schedule
import time
import shutil
import os
from datetime import datetime

source = input("Enter source file path: ")
destination = input("Enter destination directory: ")

def Backup():
    if not os.path.exists(source):
        print("Source file not found")
        return

    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    backupfile = os.path.join(destination, f"{name}_{timestamp}{ext}")

    shutil.copy(source, backupfile)

    with open("backup_log.txt", "a") as f:
        f.write("Backup completed successfully at " +
                datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    print("Backup completed successfully.")

schedule.every(1).hours.do(Backup)

while True:
    schedule.run_pending()
    time.sleep(1)