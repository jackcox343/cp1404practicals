"""
Taxi Simulator
Estimate: 60 mins
Actual:
"""


def main():
    print("Let's drive!")
    choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")
            choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()



main()
