PI = 3.14


def smallest_number(first_num, second_num):
    if(first_num < second_num):
        # print(f"{first_num} is smallest number")
        return first_num
    else:
        # print(f"{second_num} is smallest number")
        return second_num


def greatest_number(first_num, second_num):
    if(first_num > second_num):
        return first_num
    else:
        return second_num


def area_of_circle(radius):
    area = PI * radius * radius
    return area


first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
radius = int(input("Enter radius: "))

smaller_num = smallest_number(first_num, second_num)
print(smaller_num)

greater_num = greatest_number(first_num, second_num)
print(greater_num)


circle = area_of_circle(radius)
print(circle)
