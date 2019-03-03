import sys, os

status,interval,twenty,notification = sys.arg[1],sys.arg[2],sys.arg[3],sys.arg[4]

with open("engine/config.json","r") as file:
    file.readline()
    string = file.readline()
    prev_status = string.split(",")[0][-1]
file.close()

if prev_status =="0" and status == "1":
    os.system("python engine/main.py")


stats_file = open("engine/config.json","w")

stats_file.write("{\n")
stats_file.write("'start':"+str(status)+",\n")
stats_file.write("'time':"+str(time)+",\n")
stats_file.write("'twenty':"+str(twenty)+",\n")
stats_file.write("'notification':"+str(notification)+",\n}")

stats_file.close()
