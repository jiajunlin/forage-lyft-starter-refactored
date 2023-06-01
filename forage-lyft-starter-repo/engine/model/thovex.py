from datetime import datetime

from engine.engines import CapuletEngine
from engine.battery import NubbinBattery


class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        if self.needs_service():
            return True
        else:
            return False
