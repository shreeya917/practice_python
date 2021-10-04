length = float(input("Enter your length: "))
breadth = float(input("Enter your breadth: "))

display_choice = input("Enter display choice: ")

if (display_choice == "area"):
    area = length * breadth
    print(f"area = {area}")    
elif (display_choice == "perimeter"):
    perimeter = 2*(length + breadth)
    print(f"perimeter = {perimeter}")
else:
    print("invalid input")

