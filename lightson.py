import subprocess
from phue import Bridge
from datetime import datetime, timedelta

done_today = False
lights = [  {‘hue’: 25574,‘sat’: 254,‘bri’: 254, ‘transitiontime’: 3 , ‘on’: True},
            {‘hue’: 25574,‘sat’: 254,‘bri’: 254, ‘transitiontime’: 3 , ‘on’: True},
            {‘hue’: 25574,‘sat’: 254,‘bri’: 254, ‘transitiontime’: 3 , ‘on’: True}]

if __name__ == '__main__':
    while True:
        sleep(10)
        p = subprocess.Popen("arp-scan -l -r 3 | grep xx:xx:xx:xx:xx:xx", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        if output and not done_today:
            print "Smartphone is connected to the network."
            if b is None:
                b = Bridge('Bridge IP Address')
                b.connect()
            for light in lights:
                b.set_light(1 , {‘hue’: 25574,‘sat’: 254,‘bri’: 254, ‘transitiontime’: 3 , ‘on’: True})
            done_today = True
            output = None
            
        elif done_today:
            print "Sleeping until tomorrow..."
            done_today= False
            b.disconnect()
            sleep(calculatteTimeDelta())
            
            
def calculatteTimeDelta():
    now = datetime.now()
    tomorrow = now.replace(hour=17, minute=30, second=0, microsecond=0)
    return (timedelta(hours=24) - (now - tomorrow)).total_seconds() % (24 * 3600)
