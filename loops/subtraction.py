
first_num = int(input("Enter your first number: "))
second_num = int(input("Enter your second number: "))
option = 'y'
while(option != "n"):
    subtraction = first_num -  second_num
    print(f'The subtraction of {first_num} and {second_num} is {subtraction}.')
    option = input("Do you want to perform subtraction again? ")
    option = option.lower()

    if(option == "y"):
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
    else:
        print("Goodbye")
