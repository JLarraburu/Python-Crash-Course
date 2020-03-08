file_path = 'c:/Users/jonathan.larraburu/OneDrive - Solarwinds/Python Practice/Python-Crash-Course/Part 1/10 Files and Exceptions/pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

    