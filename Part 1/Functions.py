#   Functions

def greet_user():
    """Displays a simple greeting."""
    print('Hello!')

greet_user()

#   Passing information to a function
def greet_user_again(username):
    """Displays a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user_again('jesse')

#   Positional Arguments and Multiple Function Calls
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='Sugar Glider', pet_name='Flash')

#   Default Values
def describe_another_pet(pet_name, animal_type='dog'):
    """Describing some more pets here."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_another_pet('willie')

#   Return a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#   Making an Argument Optional
def optional_middle_name(first_name, last_name, middle_name=''):
    """Giving the argument a default value will make it optional"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = optional_middle_name('jimi', 'hendrix')
print(musician)

musician = optional_middle_name('john', 'hooker', 'lee')
print(musician)