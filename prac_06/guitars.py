"""
Guitar test
Estimate: 30 mins
Actual: 30 mins
"""

from prac_06.guitar import Guitar

guitars = []
print("My Guitars!")
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    print(f"{add_guitar} added.")
    name = input("Name: ")

print("... snip ...")

long_name_length = max(len(guitar.name) for guitar in guitars)

for i, guitar in enumerate(guitars, 1):
    vintage_string = "" if guitar.is_vintage() else "(Vintage)"
    print(f"Guitar {i}: {guitar.name:{long_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
