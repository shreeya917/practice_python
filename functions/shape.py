def circle(radius):
    area = PI * radius * radius
    perimeter = 2 * PI * radius
    return area, perimeter


def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


def square(length):
    area = length * length
    perimeter = 4 * length
    return area, perimeter


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
    radius = int(input("Enter radius: "))

    circle_areas = circle(radius)
    print(f"Area = {circle_areas}")

    perimeters = circle(radius)
    print(f"Perimeter = {perimeters}")

elif (number_shape == '2'):  # rectangle
    length = int(input("Enter Length: "))
    breadth = int(input("Enter Breadth: "))

    rectangle_area = rectangle(length, breadth)
    print(f"Area = {rectangle_area}")

    rectangle_perimeter = rectangle(length, breadth)
    print(f"Perimeter = {rectangle_perimeter}")

elif (number_shape == '3'):  # square
    length = int(input("Enter Length: "))

    square_area = square(length)
    print(f"Area = {square_area}")

    square_perimeter = square(length)
    print(f"Perimeter = {square_perimeter}")


elif (number_shape == '4'):  # exit
    print("Goodbye")

else:  # invalid
    print("Invalid input!!")
