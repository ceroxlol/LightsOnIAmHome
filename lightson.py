import subprocess
import time
import sys
from sun_timer import SunTimer
from device_checker import DeviceChecker
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
    ip_addresses = config['ip_addresses']
    light_names = config['light_names']

    bridge = connect_bridge(config['bridge_ip'])
	
    # yeelight_bulb = Bulb("0.0.0.0")

    sun_timer = SunTimer()

    device_checker = DeviceChecker(ip_addresses)

    while True:
        # if device_checker.device_just_connected() and sun_timer.is_night():
        if device_checker.lights_on_I_am_home():
            # Turn on hue lights
            bridge.set_light(light_names.split(',') , 'on', True)
            # Turn on yeelights
            # yeelight_bulb.turn_on()
        device_checker.update_devices()
            
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
            print("IP addresses to check for: (e.g. 192.168.0.1,192.168.0.2)")
            config['ip_addresses'] = reduce_config_element(str(input()), ip_address=True)
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
    exit(1)


if __name__ == '__main__':
    main()
