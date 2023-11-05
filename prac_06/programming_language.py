"""
Programming language
Estimate: 30 mins
Actual: 60 min
"""


class ProgrammingLanguage:
    """Programming class"""

    def __init__(self, field="", typing="", reflection=True, year=0):
        """Initialises language instances"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns string based of programming languages"""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in 1999"

    def is_dynamic(self):
        """Checks to see if dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

