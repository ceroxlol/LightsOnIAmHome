import subprocess
import time
import sys
from sun_timer import SunTimer
import pickle
import phue
import re
from phue import Bridge
from datetime import datetime, timedelta
from yeelight import Bulb

def main():
    config = read_conf()
    if config is None:
        print("Please supply a valid config.")
        exit(0)
    polling_time = config['polling_time']
    device_addresses = config['device_addresses']
    light_names = config['light_names']

    bridge = connect_bridge(config['bridge_ip'])
	
    yeelight_bulb = Bulb("0.0.0.0")

    sun_timer = SunTimer()

    while True:
        device_present = ping_devices(device_addresses)
        if device_present:
            # Turn on hue lights
            if sun_timer.is_night():
                print("It's night and you got home :)")
                bridge.set_light(light_names.split(',') , 'on', True)
            # Turn on yeelights
            # yeelight_bulb.turn_on()
            
        print("sleeping for " + str(polling_time) + " seconds...")
        time.sleep(polling_time)


def read_conf():
    try:
        with open("conf.pkl", "rb") as conf_file:
            return pickle.load(conf_file)
    except FileNotFoundError:
        print("No file found. Creating new config...")
        return create_new_config()
    except EOFError:
        print("Error with the config.pkl. Exiting...")
        exit(1)


def create_new_config():
    try:
        with open("conf.pkl", "wb") as conf_file:
            config = {}
            print("Polling time (s): ")
            config['polling_time'] = int(input())
            print("Device addresses: (e.g. 192.168.0.1,192.168.0.2)")
            config['device_addresses'] = reduce_config_element(str(input()), ip_address=True)
            print("Light names: ")
            config['light_names'] = reduce_config_element(str(input()))
            print("Bridge_ip: ")
            config['bridge_ip'] = str(input())

            pickle.dump(config, conf_file)
    except:
        print("Oh... something went wrong?")
        return

    return config


def reduce_config_element(elem, ip_address=False):
    if ip_address:
        # remove everything but a number, if it is an ipaddress
        return re.sub(r"[^\d\.\,]", "", elem)
    # remove whitespaces
    return elem.replace(" ", "")
    

def ping_devices(device_addresses):
    # 0 represents the case in which a device is present
    #if 0 in list(map(lambda device: subprocess.call(['ping', '-c', '3', device]), device_addresses)):
    for device_address in device_addresses.split(','):
        if subprocess.call(['ping', '-c', '1', device_address]) == 0:
            return True
    return False


def connect_bridge(bridge_ip):
    t_end = time.time() + 30
    message_shown = False
    print("Connecting to bridge on ip " + bridge_ip + ". Press button on bridge now.")
    while time.time() < t_end:
        try:
            bridge = Bridge(bridge_ip)
            bridge.connect()
            print("Connected to HUE bridge!")
            return bridge
        except phue.PhueRegistrationException:
            if not message_shown:
                print("Please press the link button on your bridge.")
            message_shown = True
        time.sleep(2)
    
    print("Link button not pressed within 30 seconds. Exiting...")


if __name__ == '__main__':
    main()
