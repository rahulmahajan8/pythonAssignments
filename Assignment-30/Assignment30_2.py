import schedule
import time
from datetime import datetime

def DisplayTime():
    print("Current Date and Time:",
          datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(1).minutes.do(DisplayTime)

while True:
    schedule.run_pending()
    time.sleep(1)