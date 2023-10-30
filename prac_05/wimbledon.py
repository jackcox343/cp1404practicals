"""
Wimbledon
Estimate: 40 min
Actual: 1.5 hour
"""
FILENAME = "wimbledon.csv"


def main():
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        champions_to_amount_of_wins = process_data(in_file, "Champion")
        countries_to_amount_of_wins = process_data(in_file, "Country")
        print_champions(champions_to_amount_of_wins)
        print_countries(countries_to_amount_of_wins)


def process_data(file, column_name):
    """This function will process the data"""
    key_to_amount = {}
    info_line = file.readline()
    info_line = info_line.split(",")
    index = info_line.index(column_name)
    for line in file:
        champion = line.split(",")[index]
        if champion in key_to_amount:
            key_to_amount[champion] += 1
        else:
            key_to_amount[champion] = 1
    file.seek(0, 0)
    return key_to_amount


def print_champions(champions_to_amount_of_wins):
    """This function will print champions"""
    print("Wimbledon Champions: ")
    maximum_length = max(len(champion) for champion in champions_to_amount_of_wins.keys())
    for champion in champions_to_amount_of_wins:
        print(f"{champion:{maximum_length}} {champions_to_amount_of_wins[champion]}")


def print_countries(countries_to_amount_of_wins):
    """This function will print countries"""
    print(f"These {len(countries_to_amount_of_wins)} countries have won Wimbledon: ")
    countries_that_have_won = list()
    for country in sorted(countries_to_amount_of_wins.keys()):
        countries_that_have_won.append(country)
    print(' '.join(countries_that_have_won))


main()