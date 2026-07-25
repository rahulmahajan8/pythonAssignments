import schedule
import time

def Greeting():
    print("Namskar...")

schedule.every().day.at("09:00").do(Greeting)

while True:
    schedule.run_pending()
    time.sleep(1)