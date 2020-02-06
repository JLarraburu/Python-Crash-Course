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

#   Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#   Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#   Modifying a List in a Function
#   Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot case', 'robot pendant', 'dodecahedron']
completed_models = []

#   Simulate printing each design, until none are left.
#   Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #   Simulate creating a 3D printin from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#   Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#   PAssing an arbitrary number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#   Mixing positional and arbitrary agruments
def make_another_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_another_pizza(16, 'pepperoni')
make_another_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#   Using an arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containg everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

#
#   Storing your function in Modules
#
#   Importing an entire module
#   module_name.function_name()
import pizza

pizza.making_more_pizza(16, 'pepperoni', 'mushrooms')

#   importing specific functions
#   from module_name import function_name
#   or
#   from module_name import function_0, function_1, function_2

#   Using As to give a function an Alias
#   If the name of a function you're importing might conflict with an existing name in your program 
#   or if the function name is long, you can use a short, unique alias.
#   from module_name import function_name as fn

#   from pizza import make_pizza as mp

#   You can also give a module an alias
#   import pizza as p
#   p.make_pizza()

