
# class Car():
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         #   Setting a default value for an attribute
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

#     #   Modifying an attribute method through a method
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value
#         Reject the change if it attempts to roll the odometer back
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll bak an odometer!")
    
#     #   Incrementing an attribute's value through a method
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading"""
#         self.odometer_reading += miles


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# #   Modifying an attribute's value directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(63)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(230000)
# my_used_car.read_odometer()




# #   Inheritance

# class Battery():
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=70):
#         """Initialize the battery's attributes"""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery"""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270

#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")
