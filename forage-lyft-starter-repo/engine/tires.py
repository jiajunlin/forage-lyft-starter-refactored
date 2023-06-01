from abc import ABC


class Tires(ABC):
    def needs_service(self):
        pass


class Carrigan(Tires):
    def __init__(self, tireWear):
        self.tireWear = tireWear

    def needs_service(self):
        for tires in self.tireWear:
            if tires >= 0.9:
                return True
        return False


class Octoprime(Tires):
    def __init__(self, tireWear):
        self.tireWear = tireWear

    def needs_service(self):
        if sum(self.tireWear) >= 3.0:
            return True
        return False
