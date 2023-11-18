"""
Unreliable Car
Estimate: 60 mins
Actual: 70 mins
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Class for unreliable car"""
    def __init__(self, name="", fuel=0, reliability=0.0):
        """Unreliable car initializer"""
        super().__init__(fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        """compares random number against reliability to return distance"""
        if random.randint(0, 100) < self.reliability:
            distance = super().drive(distance)
            return distance
        else:
            return 0
