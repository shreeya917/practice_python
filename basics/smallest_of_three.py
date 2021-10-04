first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
third_num = float(input("Enter third number: "))

if (first_num == second_num and first_num==third_num):
    print ("numbers are equal")

elif (first_num <= second_num and first_num <= third_num):
    print(f"The smaller num is {first_num}")
   

elif (second_num <= first_num and second_num <= third_num):
    print(f"The smaller num is {second_num}")
   
    
else:
    print(f"The smaller number is {third_num}")
   

