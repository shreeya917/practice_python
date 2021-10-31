def greatest(first_num, second_num):
    if (first_num == second_num):
        return "numbers are equal"

    elif (first_num > second_num):
        return (f"The greater number is {first_num}")

    else:
        return(f"The greater number is {second_num}")


first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

greater = greatest(first_num, second_num)
print(greater)
