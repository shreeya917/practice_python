def greatest_of_three(first_num, second_num, third_num):
    if (first_num == second_num and first_num == third_num):
        return "numbers are equal"

    elif (first_num >= second_num and first_num >= third_num):
        return (f"The greater num is {first_num}")

    elif (second_num >= first_num and second_num >= third_num):
        return(f"The greater num is {second_num}")

    else:
        return (f"The greater number is {third_num}")


first_num = input("Enter first number: ")
second_num = input("Enter second number: ")
third_num = input("Enter third number: ")

greater = greatest_of_three(first_num, second_num, third_num)
print(greater)
