# battery.py

from abc import ABC, abstractmethod
from datetime import datetime


class battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class SpindlerBattery(battery, ABC):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return self.current_date > service_threshold_date


class NubbinBattery(battery, ABC):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.current_date > service_threshold_date
