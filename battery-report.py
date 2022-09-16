
import os
import psutil


def timec(secs):
    mins, secs = divmod(secs, 60)
    hrs, mins = divmod(mins, 60)
    return "%d:%02d:%02d" % (hrs, mins, secs)

battery = psutil.sensors_battery()
print("Battery percentage : ", battery.percent, "\n")

if battery.power_plugged:
    print("Laptop is charging right now. \n")
else:
    print("Laptop is not plugged in right now. \n")
    print("Battery time left : ", timec(battery.secsleft))

print("---------------------------------- \n")

rprt = input("Would you like to create a detailed battery report? (y/yes) to accept: ")

accept = ['y', 'yes', 'Yes']

if rprt in accept:
    os.system("powercfg /batteryreport")
    



