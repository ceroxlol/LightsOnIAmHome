from astral import LocationInfo
from astral.sun import sun
from datetime import datetime

class SunTimer:
    def __init__(self):
        self.loc = LocationInfo(name='Hamburg', region='Hamburg, Germany', timezone='Europe/Berlin',
                   latitude=51.0, longitude=10.0)
        self.tzinfo = self.loc.tzinfo
        self.sun = sun(self.loc.observer, date=datetime.now(self.loc.tzinfo), tzinfo=self.loc.timezone)


    def is_night(self) -> bool:
        now = datetime.now(self.tzinfo)
        if not (self.sun['sunrise'] < now < self.sun['sunset']):
            return True
        return False