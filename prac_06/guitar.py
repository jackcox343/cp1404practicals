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

    def get_age(self,current_year=2023):
        return f"In 2023 the {self.name} is: {current_year - self.year} years old"
