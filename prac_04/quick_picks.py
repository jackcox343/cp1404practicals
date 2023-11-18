"""
Quick Picks
"""
import random

NUMBER_OF_RANDOM_INTEGERS = 6
MIN = 1
MAX = 45

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    lines = random.randint(MIN, MAX)
    for x in range(NUMBER_OF_RANDOM_INTEGERS):
        lines = random.randint(MIN, MAX)
        print(f"{lines:2}", end=" ")
    print()
