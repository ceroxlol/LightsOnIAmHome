from data.device_info import DeviceInfo
from datetime import datetime, timedelta
import subprocess

class DeviceChecker:
    def __init__(self, ip_addresses):
        self.devices = []
        for ip_address in ip_addresses.split(','):
            # avoid coldstart
            self.devices.append(DeviceInfo(ip_address, datetime.now() - timedelta(days=1)))
        # amount of minutes it takes till we perceive a device as being disconnected long enough to be actually returning home
        self.absence_time = 30


    def ping_device(self, ip_address):
        # 0 represents the case in which a device is present
        if subprocess.call(['ping', '-c', '3', ip_address]) == 0:
                return datetime.now()
        return None


    def ping_devices(self):
        for device in self.devices:
            device.reconnected = self.ping_device(device.ip_address)
            

    def get_device_last_seen(self, ip_address):
        device = list(filter(lambda device: device if device.ip_address == ip_address else None, self.devices))[0]
        return device.last_seen


    def lights_on_I_am_home(self):
        self.ping_devices()

        for device in self.devices:
            if device.reconnected is None:
                continue
            else:
                if self.check_if_device_just_connected(device):
                    return True
        
        return False

    
    def check_if_device_just_connected(self, device):
        last_seen_delta = device.reconnected - device.last_seen
        print(last_seen_delta)
        if last_seen_delta > timedelta(minutes=self.absence_time):
            return True
        return False

    
    def update_devices(self):
        for device in self.devices:
            if device.reconnected is not None:
                device.last_seen = device.reconnected