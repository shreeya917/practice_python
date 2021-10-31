def triangle_sides(first_num, second_num, third_num):
    if (first_num == second_num and first_num == third_num):
        return 'numbers are equal'

    elif (first_num <= second_num and first_num <= third_num):
        return (f"The smaller num is {first_num}")

    elif (second_num <= first_num and second_num <= third_num):
        return (f"The smaller num is {second_num}")

    else:
        return(f"The smaller number is {third_num}")


first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
third_num = float(input("Enter third number: "))

smallest = triangle_sides(first_num, second_num, third_num)
print(smallest)
