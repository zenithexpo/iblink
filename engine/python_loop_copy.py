import json
import time
import Blink_Countcopy
import datetime
import sys

stats_file = open("stats.csv","a")

def read_config():
    with open('config.js') as data_file:
        data_item = json.load(data_file)

    start = bool(data_item['status'])
    set_time = int( data_item['interval'])*60
    return(start,set_time)

stats_file = open("stats.csv","a")

start, set_time = read_config()

while start:
    end_time = time.time() + 30

    finalCount = Blink_Countcopy.CountBlink()
    print(finalCount)
    sys.stdout.flush()

    while time.time()<end_time and start:
        stats_file.write(str(datetime.datetime.now())+","+str(finalCount)+"\n")

        time.sleep(20)
        start, set_time = read_config()
