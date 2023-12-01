"""
Silver Service Taxi
Estimate: 60 mins
Actual: 70 mins
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Class inherited from Taxi for a silver service taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialises attributes"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * self.price_per_km

    def get_fare(self):
        """returns calculation of fare times the flagfall"""
        return super().get_fare() + self.flagfall * self.fanciness

    def __str__(self):
        """returns formatted string"""
        super().__str__()
        return f"{super().__str__()}, fuel={self.fuel}, plus flagfall of ${self.flagfall:.2f}"
