def triangle_perimeter(first_side, second_side, third_side):
    perimeter = first_side + second_side + third_side
    return perimeter


def triangle_area(first_side, second_side, third_side):
    s = (first_side + second_side + third_side) / 2
    area = (s*(s-first_side)*(s-second_side)*(s-third_side)) ** 0.5
    return area


first_side = float(input('Enter first side: '))
second_side = float(input('Enter second side: '))
third_side = float(input('Enter third side: '))

perimeter = triangle_perimeter(first_side, second_side, third_side)
print(perimeter)

area = triangle_area(first_side, second_side, third_side)
print(area)
