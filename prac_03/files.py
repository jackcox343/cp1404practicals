"""
Files
"""

NAME_FILE = "name.txt"
name = input("Name: ")
output_file = open(NAME_FILE, "w")
print(name, file=output_file)
output_file.close()

NAME_FILE = "name.txt"
input_file = open(NAME_FILE)
text = input_file.read()
input_file.close()
print(f"Your name is {text}")

RESULT = 0
NUMBERS_FILE = "numbers.txt"
input_file = open(NUMBERS_FILE, "r")
text = input_file.readlines(3)
input_file.close()
for line in text:
    RESULT = RESULT + int(line)
print(RESULT, end="")

RESULT = 0
NUMBERS_FILE = "numbers.txt"
input_file = open(NUMBERS_FILE, "r")
text = input_file.readlines()
input_file.close()
for line in text:
    RESULT = RESULT + int(line)
print(RESULT, end="")
