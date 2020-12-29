from dataclasses import dataclass
import ipaddress
from datetime import datetime

@dataclass
class DeviceInfo:
    """Class for keeping track of ip_address and the time it was last seen as well as reconnected."""
    ip_address: ipaddress
    last_seen: datetime
    reconnected: datetime

    def __init__(self, ip_address, last_seen):
        self.ip_address = ip_address
        self.last_seen = last_seen
        self.reconnected = None
