def triangle_sides(first_side, second_side, third_side):
    if first_side == second_side == third_side:
        return 'Equilateral triangle'

    elif first_side == second_side or second_side == third_side or third_side == first_side:
        return 'Isosceles triangle'

    else:
        return 'Scalene triangle'


first_side = float(input('Enter first side: '))
second_side = float(input('Enter second side: '))
third_side = float(input('Enter third side: '))

sides = triangle_sides(first_side, second_side, third_side)
print(sides)
