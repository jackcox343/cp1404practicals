"""
Project
Estimate: 60 mins
Actual:
"""


class Project:
    def __init__(self, name="", start_date=0, end_date=0, priority=0.0, completion=0):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.priority = priority
        self.completion = completion

    def __str__(self):
        return f"Name: {self.name} Start date: {self.start_date} End date: {self.end_date} Priority: {self.priority} Completion: {self.completion}"