from datetime import datetime

from engine.engines import WilloughbyEngine
from engine.battery import NubbinBattery


class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        if self.battery_needs_service() or self.engine_should_be_serviced():
            return True
        else:
            return False
