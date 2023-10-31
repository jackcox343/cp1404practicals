"""
Programming language
Estimate: 30 mins
Actual:
"""


class ProgrammingLanguage:
    """"""

    def __init__(self, field="", typing="", reflection=True, year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in 1999"
