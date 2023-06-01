# carfactory.py

from car import Car
from datetime import datetime
from engine.engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from engine.battery import SpindlerBattery, NubbinBattery
from engine.tires import Carrigan, Octoprime


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int, tireWear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tireWear)
        calliope = Car(engine, battery, tires)

        return calliope

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int,
                        last_service_mileage: int, tireWear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Octoprime(tireWear)
        glissade = Car(engine, battery, tires)
        return glissade

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool,
                          tireWear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tireWear)
        palindrome = Car(engine, battery, tires)
        return palindrome

    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int,
                         last_service_mileage: int, tireWear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprime(tireWear)
        rorschach = Car(engine, battery, tires)
        return rorschach

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int,
                      last_service_mileage: int, tireWear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = Carrigan(tireWear)
        thovex = Car(engine, battery, tires)
        return thovex
