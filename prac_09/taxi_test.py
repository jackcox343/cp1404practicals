"""
Taxi Test
Estimate: 30 mins
Actual: 30 mins
"""
from prac_09.taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100)
my_taxi.drive(40)
my_taxi.get_fare()
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
