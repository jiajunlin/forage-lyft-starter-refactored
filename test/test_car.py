import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Calliope(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Calliope(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Calliope(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Calliope(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.engine_should_be_serviced())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Glissade(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Glissade(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Glissade(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Glissade(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.engine_should_be_serviced())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        current_date = datetime.today().date()

        car = Palindrome(last_service_date, warning_light_is_on, current_date)
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        current_date = datetime.today().date()

        car = Palindrome(last_service_date, warning_light_is_on, current_date)
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        current_date = datetime.today().date()

        car = Palindrome(last_service_date, warning_light_is_on, current_date)
        self.assertTrue(car.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        current_date = datetime.today().date()

        car = Palindrome(last_service_date, warning_light_is_on, current_date)
        self.assertFalse(car.engine_should_be_serviced())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Rorschach(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Rorschach(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Rorschach(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Rorschach(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.engine_should_be_serviced())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Thovex(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Thovex(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        current_date = datetime.today().date()

        car = Thovex(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertTrue(car.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        current_date = datetime.today().date()
        car = Thovex(last_service_date, current_mileage, last_service_mileage, current_date)
        self.assertFalse(car.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
