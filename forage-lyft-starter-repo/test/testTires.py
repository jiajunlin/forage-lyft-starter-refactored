import unittest

from engine.tires import Carrigan, Octoprime


class TestCarrigan(unittest.TestCase):
    def test_returnsTrue(self):
        tireWear = [0.1, 0.4, 0.5, 0.9]
        tire = Carrigan(tireWear)
        self.assertTrue(tire.needs_service())

    def test_returnsFalse(self):
        tireWear = [0.1, 0.2, 0.3, 0.5]
        tire = Carrigan(tireWear)
        self.assertFalse(tire.needs_service())


class TestOctprime(unittest.TestCase):
    def test_returnsTrue(self):
        tireWear = [0.9, 0.9, 0.5, 0.9]
        tire = Octoprime(tireWear)
        self.assertTrue(tire.needs_service())

    def test_returnsFalse(self):
        tireWear = [0.1, 0.3, 0.3, 0.5]
        tire = Octoprime(tireWear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
