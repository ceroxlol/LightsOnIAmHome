# LightsOnIAmHome

Small python script for scanning after a phone device connected to the wifi. Then turning on the lights automatically once per day via access to the hue bridge.

### Setup

You need to fill in some parameters first, before you can use this script.
- Insert your device's mac address instead of 'xx:xx:xx:xx:xx:xx'
- Insert the ip address of your hue bridge instead of the string 'Bridge IP Address'
- Fill in {‘hue’: 25574,‘sat’: 254,‘bri’: 254, ‘transitiontime’: 3 , ‘on’: True} with your corresponding values. You can find the values at http://test.url
- Fill in the time from which on it shall trigger the lights on for the day.
