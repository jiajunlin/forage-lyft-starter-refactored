# carfactory.py

from car import Car
from datetime import datetime
from engine.engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from engine.battery import SpindlerBattery, NubbinBattery


class CarFactory:
    def create_calliope(self, current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int):
        calliope = Car(last_service_date, current_date)
        calliope.engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        calliope.battery = SpindlerBattery(last_service_date, current_date)
        return calliope

    def create_glissade(self, current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int):
        glissade = Car(last_service_date, current_date)
        glissade.engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        glissade.battery = SpindlerBattery(last_service_date, current_date)
        return glissade

    def create_palindrome(self, current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        palindrome = Car(last_service_date, current_date)
        palindrome.engine = SternmanEngine(last_service_date, current_date, warning_light_on)
        palindrome.battery = SpindlerBattery(last_service_date, current_date)
        return palindrome

    def create_rorschach(self, current_date: datetime, last_service_date: datetime, current_mileage: int,
                         last_service_mileage: int):
        rorschach = Car(last_service_date, current_date)
        rorschach.engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        rorschach.battery = NubbinBattery(last_service_date, current_date)
        return rorschach

    def create_thovex(self, current_date: datetime, last_service_date: datetime, current_mileage: int,
                      last_service_mileage: int):
        thovex = Car(last_service_date, current_date)
        thovex.engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        thovex.battery = NubbinBattery(last_service_date, current_date)
        return thovex
