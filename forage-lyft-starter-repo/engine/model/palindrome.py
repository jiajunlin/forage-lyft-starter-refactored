from datetime import datetime

from engine.engines import SternmanEngine
from engine.battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        if self.needs_service():
            return True
        else:
            return False
