import math

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

    square = number * number
    print(f"Square of the number = {square:.2f}")


elif (math_operation == '2'):  # cube

    cube = number * number * number

    print(f"Cube of the number = {cube:.2f}")

elif (math_operation == '3'):  # power

    power = math.pow(number, 4)

    print(f"Power of the number = {power:.2f}")

elif (math_operation == '4'):  # square root

    sqrt = math.sqrt(number)

    print(f" Square root of the number = {sqrt:.2f}")

elif (math_operation == '5'):  # cube root

    cubert = (number ** (1/3))

    print(f"Cube root of the number = {cubert:.2f}")


elif (math_operation == '6'):  # power root

    powrt = (number ** (1/4))

    print(f"Power root of the number = {powrt:.2f}")


elif (math_operation == '7'):  # exit
    print("Goodbye")

else:  # invalid
    print("Invalid input!!")
