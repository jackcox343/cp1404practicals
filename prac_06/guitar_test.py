"""
Guitar test
Estimate: 30 mins
Actual: 30 mins
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2023
"""Testing for Guitar class"""
guitar_one = Guitar("Gibson L-5 CES", 1992, 16035.40)
guitar_one_age = guitar_one.get_age(CURRENT_YEAR)
another_guitar = Guitar("Another Guitar", 2013, 200)
print(guitar_one)
print(another_guitar)


print(f"{guitar_one} get_age() - Expected 100. Got {guitar_one_age}")
print(f"{another_guitar} get_age() - Expected 9. Got {another_guitar.get_age(CURRENT_YEAR)}")
print(f"{guitar_one} is_vintage() - Expected True. Got {guitar_one.is_vintage(CURRENT_YEAR)}")
print(f"{another_guitar} is_vintage() - Expected False. Got {another_guitar.is_vintage(CURRENT_YEAR)}")