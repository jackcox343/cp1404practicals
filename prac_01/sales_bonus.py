"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

ONE_THOUSAND = 1000
TEN_PERCENT = 0.1
FIFTEEN_PERCENT = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < ONE_THOUSAND:
        bonus = sales * TEN_PERCENT
    else:
        bonus = sales * FIFTEEN_PERCENT
    print(f"Your bonus is ${bonus}")
    sales = float(input("Enter sales: $"))

