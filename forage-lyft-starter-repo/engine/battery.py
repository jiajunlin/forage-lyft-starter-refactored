# battery.py

from abc import ABC, abstractmethod
from datetime import date


class battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class SpindlerBattery(ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return self.current_date > service_threshold_date


class NubbinBattery(battery, ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.current_date > service_threshold_date
