
first_num = int(input("Enter your first number: "))
second_num = int(input("Enter your second number: "))
option = 'y'
while(option != "n"):
    multiplication = first_num  *  second_num
    print(f'The multiplication of {first_num} and {second_num} is {multiplication}.')
    option = input("Do you want to perform  multiplication? ")
    option = option.lower()

    if(option == "y"):
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
    else:
        print("Goodbye")
