option = 'y'

while(option.lower() == "y"):
    first_num = int(input("Enter your first number: "))
    second_num = int(input("Enter your second number: "))

    addition = first_num + second_num
    print(f'The addition of {first_num} and {second_num} is {addition}.')

    option = input("\nDo you want to continue (y/n)? ")

print("Goodbye")
