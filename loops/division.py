option = 'y'
while(option.lower() == "y"):
    first_num = int(input("Enter your first number: "))
    second_num = int(input("Enter your second number: "))

    division = first_num / second_num
    print(f'The division of {first_num} and {second_num} is {division}.')
    
    option = input("\nDo you want to continue? ")
   


print("Goodbye")
