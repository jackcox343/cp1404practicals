from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Unreliable Car", 50, 80)
distance = int(my_car.drive(10))
print(f"{my_car.name}, {distance}km")
