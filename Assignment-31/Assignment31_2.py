import schedule
import time

def DisplayMessage(message):
    print(message)

msg = input("Enter message: ")

schedule.every(5).seconds.do(DisplayMessage, msg)

while True:
    schedule.run_pending()
    time.sleep(1)