print("""
Operations
1. Addition
2. Subtraction
3. Multilpication
4. Division
5. Exit
""")


operation = input("Enter your operation: ")
if (operation < '5'):
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: " ))

    if(operation == '1'):  # Addition
        addition = first_num + second_num
        print(f"{first_num} + {second_num} = {addition} ")

    elif(operation == '2'):  # Subtraction
        subtraction = first_num - second_num
        print(f"{first_num} - {second_num} = {subtraction} ")

    elif(operation == '3'):  # Multiplication
        multiplication = first_num * second_num
        print(f"{first_num} * {second_num} = {multiplication} ")

    elif (operation == '4'):  # Division
        division = first_num / second_num
        print(f"{first_num} / {second_num} = {division} ")

elif (operation == '5'):  # exit
    print("Goodbye")
else:
    print("Invalid input")
