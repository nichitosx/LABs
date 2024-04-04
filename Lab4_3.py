import datetime
import time

for _ in range(5):
    current_time = datetime.datetime.now()
    print(current_time.strftime("%H:%M:%S"))
    time.sleep(1)