# LightsOnIAmHome

Python to automatically turn on the lights based on ip addresses for e.g. your cellphone and wether the sun is already set or not. If a certain device is connecting to your wifi and this device has been away for a longer period of time, the script automatically turns on predefined hue lamps.

### Prerequisites
- Static IP for the hue bridge.
- IP addresses of your devices.
- Install arp-scan for scanning your lan environment. 
	`sudo apt-get install arp-scan`
- Install philips hue library.
	`pip3 install phue`
- (Optional:) Install yeelight library.
	`pip3 install yeelight`
- Devices need to be in the same network as your bridge.

### Setup
Upon start, the script is creating a configuration file which will then be used during runtime. It will ask you for:
- The polling time. The amount of seconds the script sleeps until it scans for your devices another time.
- The ip addresses from the devices you want to scan for. You can set up any amount of devices you want to scan for. Of course this data is only persisted in the conf file / during runtime.
- The names of your hue devices (the ones used in your hue app on your smartphone).
- The (static) ip address of your hue bridge.

### Run
The program can be run by executing
`python3 lightson.py`
For the first run, the script will create a configuration file. This file will be used for subsequent runs. In case you want to recreate its content, delete it and restart the script.
Furthermore, the script will initialize the DeviceInfo object with a date set to yesterday, so as a cold start, the lights will go on even if you start the script past sunset and all your devices are already connected.

### References
For further information regarding the `phue` package, please visit https://github.com/studioimaginaire/phue