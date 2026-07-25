import schedule
import time

def Coding():
    print("Coding Kar..!")

schedule.every(30).minutes.do(Coding)

while True:
    schedule.run_pending()
    time.sleep(1)