#   Working with Lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("Thank you, everyone.  That was a great magic show!")

#   Using the range() function
for value in range(1,5):
    print value

numbers = list(range(1,6))
print(numbers)

#   Print even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

#   Squares
squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)

#   List Comprehensions
#       A LC allows you to generate the same list in just one line of code
squares = [value**2 for value in range(1,11)]
print(squares)


#   Working with Part of a List

#   Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print([0:3])

#   Looping through a slice
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#   Copying a List
#       By emitting the indexes here you are essentially copying from beginning to end
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = [my_foods[:]]


#   Tuples
#       A list that cannot be changed

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#   You cannot modify a tuple.  However, you can over write the variable
dimensions = (400, 100)

#   PEP8 has all the guidelines for styling Python code
#   https://python.org//dev/peps/pep-0008/




