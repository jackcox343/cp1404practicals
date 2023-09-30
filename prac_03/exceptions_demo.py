"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
"""
When will a ValueError occur?
A value error will occur when user gives and invalid value to a function but is a valid argument.

When will a ZeroDivisionError occur?
A zero division error will occur when a number is attempted to be divided by zero.

Could you change the code to avoid the possibility of a ZeroDivisionError?
You can write an except of zerodivsionerror in the code

If you could figure out the answer to question 3, then make this change now.
"""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ZeroDivisionError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
