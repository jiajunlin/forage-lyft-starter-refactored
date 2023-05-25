from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class CapuletEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        super().__init__(last_service_date, current_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000


class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_date, warning_light_is_on, current_date):
        super().__init__(last_service_date, current_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False


class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        super().__init__(last_service_date, current_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
