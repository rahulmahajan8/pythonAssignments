import schedule
import time
import os
from datetime import datetime

directory = input("Enter directory path: ")

def CountFiles():
    if not os.path.exists(directory):
        print("Directory not found.")
        return

    count = 0

    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            count += 1

    with open("DirectoryCountLog.txt", "a") as f:
        f.write("Directory: " + directory + "\n")
        f.write("Files: " + str(count) + "\n")
        f.write("Date & Time: " +
                datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

    print("Entry Added.")

schedule.every(5).minutes.do(CountFiles)

while True:
    schedule.run_pending()
    time.sleep(1)