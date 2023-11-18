"""
Taxi Simulator
Estimate: 60 mins
Actual:
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                pass
        else:
            print("Invalid option")
            choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()


def choose_taxi(taxis):
    print(f"Taxis available:\n{display_taxi(taxis)} ")
    taxi_choice = input("Choose taxi: ")
    try:
        taxi_choice = int(taxi_choice)
        if taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
