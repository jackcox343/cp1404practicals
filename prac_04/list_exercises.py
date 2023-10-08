"""
List Exercises
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
average = sum(numbers) / len(numbers)
print(f"The first number is {numbers[0]}\nThe last number is {numbers[4]}"
      f"\nThe smallest number is {min(numbers)}\nThe largest number is {max(numbers)}\n"
      f"The average of the numbers is {average}")
