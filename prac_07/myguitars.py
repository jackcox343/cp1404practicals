from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    FILENAME = "guitars.csv"

    guitars = read_guitars(FILENAME)

    get_new_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)


def get_new_guitars(guitars):
    """This function will get new guitars"""
    name = input("Guitar name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)


def read_guitars(FILENAME):
    """This function reads file to list"""
    guitars = []
    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, year, cost = parts
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    file.close()
    return guitars


def display_guitars(guitars):
    """This function displays guitars line by line"""
    for guitar in guitars:
        print(guitar)


main()
