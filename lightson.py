import subprocess
import time
import sys
from phue import Bridge
from datetime import datetime, timedelta

bridge_ip = None
device_address = None
b = None

def calculateTimeDelta(hour, minute):
    now = datetime.now()
    tomorrow = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    return (timedelta(hours=24) - (now - tomorrow)).total_seconds() % (24 * 3600)

if __name__ == '__main__':
    done_today = False
    polling_time = int(sys.argv[1])
    hour, minute = sys.argv[2].split(":")
    device_address = sys.argv[3]
    bridge_ip = sys.argv[4]
	
    hour = int(hour)
    minute = int(minute)

    while True:
        res = subprocess.call(['ping', '-c', '3', device_address])
        if res == 0 and not done_today:
            print("Device is connected to the network.")
            if b is None:
                b = Bridge(bridge_ip)
                print("Connecting to bridge on ip " + bridge_ip + ". Press button on bridge now.")
                b.connect()
            b.set_light(['DEVICE1', 'DEVICE2'] , 'on', True)
            done_today = True
            
        elif done_today:
            done_today= False
            print("Sleeping until tomorrow... ("+str(calculateTimeDelta(hour, minute))+" seconds)")
            time.sleep(calculateTimeDelta(hour, minute))
        print("sleeping for " + str(polling_time) + " seconds...")
        time.sleep(polling_time)
