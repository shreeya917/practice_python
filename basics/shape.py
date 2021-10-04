PI = 3.14

print("""
Choose your Shape
    1. Circle
    2. Rectangle
    3. Square
    4. Exit
    """)
number_shape = input("Enter Option: ")

if (number_shape == '1'):  # circle
    radius = float(input("Enter radius: "))

    area = PI * radius * radius
    perimeter = 2 * PI * radius

    print(f"Area = {area:.2f}")
    print(f"Perimeter = {perimeter:.2f}")

elif (number_shape == '2'):  # rectangle
    length = float(input("Enter Length: "))
    breadth = float(input("Enter Breadth: "))

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f"Area = {area:.2f}")
    print(f"Perimeter = {perimeter:.2f}")


elif (number_shape == '3'):  # square
    length = float(input("Enter Length: "))

    area = length * length
    perimeter = 4 * length

    print(f"Area = {area:.2f}")
    print(f"Perimeter = {perimeter:.2f}")


elif (number_shape == '4'):  # exit
    print("Goodbye")

else:  # invalid
    print("Invalid input!!")
