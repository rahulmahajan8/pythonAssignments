import schedule
import time

schedule.every(int(sys.argv[2])).minutes.do(
    lambda: DeleteDuplicates(FindDuplicate(Directory))
)

while True:
    schedule.run_pending()
    time.sleep(1)