"""Passwrod Stars"""


def main():
    PASSWORD = "Pythonista"
    password = get_password(PASSWORD)
    print_asterisk(password)


def get_password(PASSWORD):
    """This will get password over minimum set"""
    password = input("Password: ")
    while len(password) < len(PASSWORD):
        print("Password doesnt meet minimum length.")
        password = input("Password: ")
    return password


def print_asterisk(password):
    """This will print stars"""
    for i in range(0, len(password), 1):
        print("*", end="")


main()
