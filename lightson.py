import subprocess
import time
import sys
from phue import Bridge
from datetime import datetime, timedelta

bridge_ip = None
device_address = None

if __name__ == '__main__':
    done_today = False
    polling_time = int(sys.argv[1])
    hour, minute = sys.argv[2].split(":")
    device_address = sys.argv[3]
    bridge_ip = sys.argv[4]

    while True:
        time.sleep(polling_time)
        p = subprocess.Popen("sudo arp-scan -l -r 3 | grep " + device_address, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        if output and not done_today:
            print("Device is connected to the network.")
            if b is None:
                b = Bridge(bridge_ip)
                print("Connecting to bridge on ip " + bridge_ip + ". Press button on bridge now.")
                b.connect()
            b.set_light(['DEVICE1', 'DEVICE2'] , 'on', True)
            done_today = True
            output = None
            
        elif done_today:
            print("Sleeping until tomorrow...")
            done_today= False
            time.sleep(calculatteTimeDelta(hour, minute))
            
            
def calculatteTimeDelta(hour, minute):
    now = datetime.now()
    tomorrow = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    return (timedelta(hours=24) - (now - tomorrow)).total_seconds() % (24 * 3600)
