import math


def square(number):
    square = number * number
    return square


def cube(number):
    cube = number * number * number
    return cube


def power(number):
    power = math.pow(number, 4)
    return power


def square_root(number):
    square_root = math.sqrt(number)
    return square_root


def cube_root(number):
    cube_root = (number ** (1/3))
    return cube_root


def power_root(number):
    power_root = (number ** (1/4))
    return power_root


print("""
Choose Math operation  you like to perform
    1. Square
    2. Cube
    3. Power
    4. Square root
    5. Cube root
    6. Power root
    7. Exit
    """)
math_operation = input("Enter Option: ")
number = float(input("Enter a number: "))

if (math_operation == '1'):  # square

    sq = square(number)
    print(f"Square of the number = {sq:.2f}")


elif (math_operation == '2'):  # cube

    cub = cube(number)

    print(f"Cube of the number = {cub:.2f}")

elif (math_operation == '3'):  # power

    powe = power(number)

    print(f"Power of the number = {powe:.2f}")

elif (math_operation == '4'):  # square root

    sqrt = square_root(number)

    print(f" Square root of the number = {sqrt:.2f}")

elif (math_operation == '5'):  # cube root

    cubert = cube_root(number)

    print(f"Cube root of the number = {cubert:.2f}")


elif (math_operation == '6'):  # power root

    powrt = power_root(number)

    print(f"Power root of the number = {powrt:.2f}")


elif (math_operation == '7'):  # exit
    print("Goodbye")

else:  # invalid
    print("Invalid input!!")
