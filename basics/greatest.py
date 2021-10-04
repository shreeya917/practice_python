first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

if (first_num == second_num):
    print ("numbers are equal")

elif (first_num > second_num):
    print(f"The greater number is {first_num}")
    print(f"The smaller number is {second_num}")
    
else:
    print(f"The greater number is {second_num}")
    print(f"The smaller number is {first_num}")

