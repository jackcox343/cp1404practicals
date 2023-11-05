from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    FILENAME = "guitars.csv"
    guitars = read_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)


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
