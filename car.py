from abc import ABC, abstractmethod


class serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return
