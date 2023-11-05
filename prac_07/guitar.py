"""
Guitar
Estimate: 30 mins
Actual: 40 mins
"""


class Guitar:
    """Class for guitar to store guitars"""

    def __init__(self, name="", year=0, cost=0):
        """Initialises guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns string of guitar information"""
        return f"{self.name} ({self.year}) : {self.cost}"

    def __lt__(self, other):
        """Compares objects based off year"""
        return self.year < other.year

    def get_age(self, current_year=2023):
        """returns age of guitar"""
        return current_year - self.year

    def is_vintage(self, current_year=2023):
        """returns boolean if guitar equal or over 50"""
        return current_year - self.year >= 50
