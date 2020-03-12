# LightsOnIAmHome

Small python script for scanning after a phone device connected to the wifi. Then turning on the lights automatically once per day via access to the hue bridge.

### Prerequisites
- Static IP for the hue bridge.
- MAC address of your device.
- Install arp-scan for scanning your lan environment. 
	`sudo apt-get install arp-scan`
- Install philips hue library.
	`pip3 install phue`
- Install yeelight library.
	`pip3 install yeelight`

### Setup
You need to fill in some parameters first, before you can use this script.
- Insert your device's mac or ip address instead of 'xx:xx:xx:xx:xx:xx'.
- Insert the ip address of your hue bridge into bridge_ip. If you don't want to assign a static ip, feel free to call the program with the corresponding ip.
- Fill in your Devices. If you want to only adjust one device, leave out the parenthesis. For further choices go to https://github.com/studioimaginaire/phue
- Hand over the time in the format "HH:MM" from which the lights shall trigger for the day.

### Run
The program can be run by executing
`python3 lightson.py POLLING_TIME HH:MM [DEVICE_ADRESS] [BRIDGE_IP]`
DEVICE_ADRESS and BRIDGE_IP are optional and my be constantly written into the python file.
You might need to add `sudo -u YOUR_USER` to execute the program with priviledged rights as the subprocess execution needs those.
