file_name = 'alice.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)