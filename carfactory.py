# carfactory.py

from car import Car
from datetime import datetime
from engine.engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from engine.battery import SpindlerBattery, NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(engine, battery)
        return calliope

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(engine, battery)
        return glissade

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        engine = SternmanEngine(last_service_date, current_date, warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(engine, battery)
        return palindrome

    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int,
                         last_service_mileage: int):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        battery = NubbinBattery(last_service_date, current_date)
        rorschach = Car(engine, battery)
        return rorschach

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int,
                      last_service_mileage: int):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, current_date)
        battery = NubbinBattery(last_service_date, current_date)
        thovex = Car(engine, battery)
        return thovex
