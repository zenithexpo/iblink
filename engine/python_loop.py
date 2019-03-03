import json
import time
import Blink_Count
import datetime
import sys
import threading

def twenty_rule():
    print("Reminder")
    sys.stdout.flush()
    threading.Timer(1200,twenty_rule).start()

twenty_rule()

stats_file = open("engine/stats.csv","a")

def read_config():
    with open('config.js') as data_file:
        data_item = json.load(data_file)

    start = bool(data_item['status'])
    set_time = int( data_item['interval'])*60
    return(start,set_time)

stats_file = open("engine/stats.csv","a")

start, set_time = read_config()



while start:
    end_time = time.time() + set_time - 60
    #end_time = time.time() + 30


    finalCount = Blink_Count.CountBlink()

    if finalCount != -1:
        print(finalCount)
        sys.stdout.flush()
        stats_file.write(str(datetime.datetime.now())+","+str(finalCount)+"\n")
    else:
        start = False

    while time.time()<end_time and start:
        time.sleep(3)
        start, set_time = read_config()
