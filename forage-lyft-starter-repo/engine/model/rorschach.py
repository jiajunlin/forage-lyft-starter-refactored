from datetime import datetime

from engine.engines import WilloughbyEngine
from engine.battery import NubbinBattery


class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        if self.needs_service():
            return True
        else:
            return False
