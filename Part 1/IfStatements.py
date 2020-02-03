#   If Statements

#   Simple example

cars = ['audi', 'bmw', 'subaru', 'toyota']

#   Note that this is case sensitive and you can use .lower() or .upper()
for car in cars :
    if car == 'bmw' : 
        print(car.upper())
    else:
        print(car.title())

#   All the usual operators ==, !=, >=, <=, and, or

#   Checking Whether a Value is in a List

if 'audi' in cars :
    print('True')
else:
    print('false')

#   Checking if NOT in a list
if 'audi' not in cars :
    print('True')
else:
    print('false')

