"""
Taxi Simulator
Estimate: 60 mins
Actual:
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main function for taxi simulation program"""
    current_taxi = None
    bill_to_date = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while choice != "q":
        if choice == "c":
            print(f"Taxis available:")
            display_taxi(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                cost = current_taxi.drive(distance)
                bill_to_date += cost
                print(f"Your {current_taxi.car_name} trip cost you ${cost:.2f}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date}")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxi(taxis)


def choose_taxi(taxis):
    """Chooses valid taxi input"""
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
    """Displays taxis enumerated"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
