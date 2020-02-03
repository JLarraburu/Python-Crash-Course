#   Python Crash Course
#   Jonathan Larraburu

print ("Hello World!")

#   Variables
message = "Hello Python World!  This string is saved to a variable."
print(message)

variable_rules = "Variable names can contain only letters, numbers, and underscores.  They can start with a letter or an underscore, but not with a number."

variable_rules_ext = variable_rules

print(variable_rules_ext)

#   Strings
simple = 'strings are very simple in Python'
example_string = "I can use quotes or apostrophes 'or both'"
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())
first_name = 'jon'
last_name = 'larraburu'
full_name = first_name + ' ' + last_name
print(full_name)
print('Hello, ' + full_name.title() + '!')
print('\t This will add a tab.')
print('\nThis is add a new line.  This one is very convenient if you remember c++')
print('combine the two...\n')
print('\tLanguages:\n')
print('\t\tPython!')
print('\t\tC++!')
print('\t\tJavaScript!')
stripping_whitespace = 'python '
stripping_whitespace.rstrip()
print(stripping_whitespace)
stripping_whitespace = stripping_whitespace.rstrip()
print(stripping_whitespace)

#   Numbers
this_is_how_exponents_work = 2 ** 8
age = 32
happy_birthday = 'Happy ' + str(age) + 'nd birthday!'

#   I know how comments work!
#   We love comments!
#   More comments the better!
#   The main reason to write comments is to explain what your code is supposed to do and how you are making it work.
""" There is no reason you can't use this as a 
    multiline comment when writing python."""
#   Still cleaner to just use comments imo