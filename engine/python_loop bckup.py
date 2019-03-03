import json
import time
import Blink_Count
import datetime
import sys


def read_config():
    with open('config.js') as data_file:
        data_item = json.load(data_file)

    start = bool(data_item['status'])
    set_time = int( data_item['interval'])*60
    return(start,set_time)

stats_file = open("engine/stats.csv","a")

start, set_time = read_config()

while start:
    end_time = time.time() + set_time

    finalCount = Blink_Count.CountBlink()

    stats_file.write(str(datetime.datetime.now())+","+str(finalCount)+"\n")
    print(finalCount)
    sys.stdout.flush()

    remaining_time = end_time - time.time()
    if remaining_time>0:
        time.sleep(remaining_time)

    start, set_time = read_config()
