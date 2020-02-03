#   Introducing Lists
#   A list is a collection of items in a particular order.
bicycles = ['trek', 'specialized', 'redline']
print(bicycles[0])
print(bicycles[0].title())

#   By using the index -1 you can pull the last item in the list
print(bicycles[-1])
#   This extends to other negative positions
print(bicycles[-2])

#   Adding elements to a list with append()
bicycles.append('Some shit!')
#   The append() method makes it easy to make lists dynamically
shoes = []
shoes.append('nike')
shoes.append('adidas')
shoes.append('reebok')
shoes.append('vans')

#   inserting items into a list using insert()
shoes.insert(0, 'ugg')

#   Removing an item from a list with the del statement
del shoes[0]

print(shoes.pop())
print(shoes.pop(2))

#   Organizing a List

#   Sort
cars = ['bmw', 'audi', 'toyota', 'subaru', 'volkswagen']
print(cars)

#   Temporary sort
print(sorted(cars))
print(cars)

#   Perma-sort
cars.sort()
print(cars)

cars.reverse()
print(cars)

#   Finding the length of a list
len(cars)