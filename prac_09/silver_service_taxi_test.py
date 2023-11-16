from prac_09.silver_service_taxi import SilverServiceTaxi

my_silver_service_taxi = SilverServiceTaxi("Silver Taxi", 50, 2)
my_silver_service_taxi.drive(18)
new_fare = my_silver_service_taxi.get_fare()
print(new_fare)
