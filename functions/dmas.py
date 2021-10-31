def addition(first_num, second_num):
    addition = first_num + second_num
    return addition


def subtraction(first_num, second_num):
    subtraction = first_num - second_num
    return subtraction


def multiplication(first_num, second_num):
    multiplication = first_num * second_num
    return multiplication


def division(first_num, second_num):
    division = first_num / second_num
    return division


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
    second_num = float(input("Enter second number: "))

    if(operation == '1'):  # Addition
        add = addition(first_num, second_num)
        print(f"{first_num} + {second_num} = {add} ")

    elif(operation == '2'):  # Subtraction
        sub = subtraction(first_num, second_num)
        print(f"{first_num} - {second_num} = {sub} ")

    elif(operation == '3'):  # Multiplication
        mul = multiplication(first_num, second_num)
        print(f"{first_num} * {second_num} = {mul} ")

    elif (operation == '4'):  # Division
        div = division(first_num, second_num)
        print(f"{first_num} / {second_num} = {div} ")

elif (operation == '5'):  # exit
    print("Goodbye")
else:
    print("Invalid input")
