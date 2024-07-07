"""Score Menu"""

MENU = "(G)et a valid score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit"


def main():
    print(MENU)
    choice = input("Choice: ").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
            print(MENU)
            choice = input("Choice: ").lower()
            if choice == "p":
                score = print_result(score)
                print(score)
                print(MENU)
                choice = input("Choice: ").lower()
            elif choice == "s":
                print_stars(score)
                print(MENU)
                choice = input("Choice: ").lower()
    else:
        print("Good Bye")


def print_stars(score):
    """This will print stars"""
    for i in range(0, score):
        print("*" , end="")
    print()


def print_result(score):
    """This will sort category"""
    if score >= 90:
        score = "Excellent"
    elif score >= 50:
        score = "Pass"
    else:
        score = "Bad"
    return score


def get_valid_score():
    """This will error check"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score





main()
