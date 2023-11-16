"""
Unreliable Car
Estimate: 60 mins
Actual:
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=0.0):
        super().__init__(fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):

        if random.randint(0, 100) < self.reliability:
            distance = super().drive(distance)
            return distance
        else:
            return 0
