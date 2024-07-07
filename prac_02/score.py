"""
CP1404- Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    score_category = get_score(score)
    random_score = random.randint(0, 100)
    random_score_category = get_score(random_score)
    print(f"User Score: {score} \nScore Category: {score_category}")
    print(f"Random Score: {random_score} \nRandom Score Category: {random_score_category}")


def get_score(score):
    """Will return score category"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
