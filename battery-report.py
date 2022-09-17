import os
try:
    import psutil
except:
    os.system("pip install psutil")
    import psutil
from datetime import datetime


os.system("cls")


print(datetime.now())

def timec(secs):
    mins, secs = divmod(secs, 60)
    hrs, mins = divmod(mins, 60)
    return "%d:%02d:%02d" % (hrs, mins, secs)

battery = psutil.sensors_battery()
print("\n \nBattery percentage : ", battery.percent, "\n")

if battery.power_plugged:
    print("Laptop is charging right now. \n")
else:
    print("Laptop is not plugged in right now. \n")
    print("Battery time left : ", timec(battery.secsleft))

print("---------------------------------- \n")
accept = ['y', 'yes', 'Yes']
rprt = input("Would you like to create a detailed battery report? (y/yes) to accept: ")



if rprt in accept:
   os.system("powercfg /batteryreport")

rprt2 = input("would you like to log this info in a txt file? (y/yes) to accept: ")
if rprt2 in accept:
    SaveFile = open("ChargeStats.txt", "a")
    SaveFile.write(f"{datetime.now()}")
    SaveFile.write(f"\n \nBattery percentage : {battery.percent} \n")
    if battery.power_plugged:
        SaveFile.write("Laptop is charging right now. \n")
        SaveFile.write("---------------------------------- \n")
    else:
        SaveFile.write("Laptop is not plugged in right now. \n")
        SaveFile.write(f"Battery time left : {timec(battery.secsleft)} \n")
        SaveFile.write("---------------------------------- \n")
    SaveFile.close()
if rprt in accept:
    os.system("battery-report.html")

print("Process is finished.")
    


    
