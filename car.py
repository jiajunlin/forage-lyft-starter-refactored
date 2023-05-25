from abc import ABC, abstractmethod
from datetime import datetime
from engine.engines import Engine
from engine.battery import battery


class serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(serviceable):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.engine = Engine()
        self.battery = battery()

    def needs_service(self):
        return
