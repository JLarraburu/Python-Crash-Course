#   Dictionaries

#   A simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#   you can use the str() function to turn an integer into a string
print(str(alien_0['points']))

print(alien_0)

#   Adding key-pairs to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#   Starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
alien_1['x_position'] = 25
alien_1['y_position'] = 100
print(alien_1)

#   Modifying is exactly how you think it is
alien_1['color'] = 'Magenta'
print(alien_1)

#   Position of an alien that can move at different speeds
alien_1['speed'] = 'medium'
print("Original X position: " + str(alien_1['x_position']))

#   Move the alien to the right
#   Determine how far to mvoe the alien based on its current speed
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

#   The new position is the old position plus the increment
alien_1['x_position'] = alien_1['x_position'] + x_increment
print("New x_position: " + str(alien_1['x_position']))

#   To remove an entry use the del statement, This is permenant
del alien_1['points']
print(alien_1)

#   Dictionaries can be written like this for brevity...
favorite_languages = {
    'Jon' : 'Python',
    'Aoife' : 'JavaScript',
    'Patrick' : 'C++',
    }

#   Looping through a dictionary
user_0 = {
    'username' : 'efermi',
    'first' : 'enrice',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#   these names can be anything
for name, language in favorite_languages.items():
    print(name + " loves " + language)

#   Looping through keys is the default behavior
for name in favorite_languages:
    print(name)

for name in favorite_languages.keys():
    print(name)

#   Looping through a dictionary's keys in order
#   This sorts before looping
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#   Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#   You can wrap favorite_languages.values() in a set() function to only show unique values
#   For example, set(favorite_languages.values())

#   Nesting
#   A list of Dictionaries

alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens :
    print(alien)

#   Make an empty list for storing aliens
aliens = []

#   Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color' : 'green', 'points' : 5}
    aliens.append(new_alien)

#   Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

