#   User Input and While Loops

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
age = int(age)
if (age >= 18) :
    print("Hiya")

#   Modulo operator practice
number = input("Enter a number, and I will tell you if it's even or odd. ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

#Introducing while loops
current_number = 1
while current_number <= 5 :
    print(current_number)
    current_number += 1
#   Using a while loop to run the program until the user wants to quit
prompt = "\nTell me something, and I will repeat is back to you:"
prompt += "\nEnter 'quit to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#   Using a flag to monitor whether or not the program should continue running
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#   A break statement works exactly how you think it does
#   You can use a break statement in any Python loop
prompt = "What's your favorite city? "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# The continue statement returns you to the beginning of a loop

current_number = 0
while current_number < 10:
    current_number += 1
    # If current_number is even
    if current_number % 2 == 0:
        continue
    print(current_number)

#   Using a while loop with lists and dictionaries

#   Moving items from one list to another

#   Start with users that need to be verified,
#   and an empy list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#   Verify each user until there are no more unconfirmed users.
#   Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

#   Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#   Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)