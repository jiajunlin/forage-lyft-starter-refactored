from datetime import datetime

from engine.engines import SternmanEngine
from engine.battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        if self.battery_needs_service() or self.engine_should_be_serviced():
            return True
        else:
            return False
