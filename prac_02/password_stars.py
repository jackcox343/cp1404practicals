PASSWORD = "Pythonista"
password = input("Password: ")
while len(password) < len(PASSWORD):
    print("Password doesnt meet minimum length.")
    password = input("Password: ")
for i in range(0, len(password), 1):
    print("*", end="")
