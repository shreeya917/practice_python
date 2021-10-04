first_side = float(input('Enter first side: '))
second_side = float(input('Enter second side: '))
third_side = float(input('Enter third side: '))

if first_side == second_side == third_side:
    print("Equilateral triangle")

elif first_side == second_side or second_side == third_side or third_side == first_side:
    print("Isosceles triangle")

else:
    print("Scalene triangle")
