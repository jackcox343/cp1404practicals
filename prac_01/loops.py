for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
A
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""
B
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
C
"""
number = int(input("Number: "))
print(f"Number of stars: {number}")
for i in range(0, number, 1):
    print(end='*')

"""
D
"""
number = int(input("Number: "))
for i in range(0, number, 1):
    for x in range(0, i + 1, 1):
        print(end='*')
    print()
