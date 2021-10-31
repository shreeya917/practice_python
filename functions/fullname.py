
def fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return ("Your fullname is " + full_name)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

name = fullname(first_name, last_name)
print(name)
