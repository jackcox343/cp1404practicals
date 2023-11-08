"""
Project
Estimate: 60 mins
Actual: 120 mins
"""


class Project:
    """This represents project class"""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion=0):
        """This initialises the project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """This returns string formatted"""
        return f"{self.name} Start: {self.start_date}, Priority {self.priority},Estimate: {self.cost_estimate}, Completion: {self.completion}%"

    def __lt__(self, other):
        """This compares two priority ratings"""
        return self.priority < other.priority

    def is_complete(self):
        """This checks completion"""
        return self.completion == 100
