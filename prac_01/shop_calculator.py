TOTAL_PRICE = 0
TEN_PERCENT_DISCOUNT = 0.1
ONE_HUNDRED = 100
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items, 1):
    item_price = float(input("Price of items: "))
    TOTAL_PRICE = TOTAL_PRICE + item_price
if TOTAL_PRICE > 100:
    discount_price = TOTAL_PRICE * TEN_PERCENT_DISCOUNT
    TOTAL_PRICE = TOTAL_PRICE - discount_price
print(f"Total price for {number_of_items} items is ${TOTAL_PRICE:.2f}")
