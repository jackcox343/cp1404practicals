"""
Guitar
Estimate: 60 mins
Actual:
"""


class Guitar:
    """Class for guitar to store guitars"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} {self.year} : {self.cost}"

    def get_age(self, current_year=2023):
        return current_year - self.year

    def is_vintage(self, current_year=2023):
        result = self.get_age()
        return result >= 50
