import unittest
from datetime import date, datetime

from engine.engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from engine.battery import SpindlerBattery, NubbinBattery


class TestEngines(unittest.TestCase):
    def testCapuletEngineTrue(self):
        current_mileage = 40000
        last_service_mileage = 9000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def testCapuletEngineFalse(self):
        current_mileage = 29000
        last_service_mileage = 14000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

    def testGlissadeEngineTrue(self):
        current_mileage = 69000
        last_service_mileage = 9000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def testGlissadeEngineFalse(self):
        current_mileage = 29000
        last_service_mileage = 14000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

    def testSternmanEngineTrue(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def testSternmanEngineFalse(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())



class TestBatteries(unittest.TestCase):
    def testSpindlerBatteryTrue(self):
        last_service_date = date.fromisoformat('2021-05-23')
        current_date = datetime.today().date()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def testSpindlerBatteryFalse(self):
        last_service_date = date.fromisoformat('2021-11-23')
        current_date = datetime.today().date()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def testNubbinBatteryTrue(self):
        last_service_date = date.fromisoformat('2018-05-23')
        current_date = datetime.today().date()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def testNubbinBatteryFalse(self):
        last_service_date = date.fromisoformat('2022-11-23')
        current_date = datetime.today().date()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
