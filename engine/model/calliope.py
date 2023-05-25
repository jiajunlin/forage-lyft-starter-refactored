from datetime import datetime

from engine.engines import CapuletEngine
from engine.battery import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        if self.battery_needs_service() or self.engine_should_be_serviced():
            return True
        else:
            return False
