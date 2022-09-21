from datetime import datetime 
import os 
import time 
import psutil 



#set the timezone to your timezone, find the name in /usr/share/zoneinfo/
current_time = "if you are seeing this something went wrong"
current_timezone = "America/New_York"
cmd = 'xsetroot -name "%s"' % (current_time)


while True:
    time.sleep(1)
    current_time = datetime.utcnow()
    current_time = str(current_time)
    current_time_short = current_time[0:16]
    #full disclosure I stole this next part line for line from somethine online
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    stringpercent = str(battery.percent)
    thisisdumb = stringpercent[0:2]
    percent = thisisdumb + "%"
    plugged = "AC" if plugged else "Battery"
    os.system('xsetroot -name "%s - %s %s "' % (current_time_short, percent, plugged))

