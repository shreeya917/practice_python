
def area_rectangle(length, breadth):
    area = length * breadth
    return area


def perimeter_rectangle(length, breadth):
    perimeter = 2*(length + breadth)
    return perimeter


length = float(input("Enter your length: "))
breadth = float(input("Enter your breadth: "))

display_choice = input("Enter display choice: ")

if (display_choice == "area"):
    area_rec = area_rectangle(length, breadth)
    print(area_rec)

elif (display_choice == "perimeter"):
    peri_rec = perimeter_rectangle(length, breadth)
    print(peri_rec)
else:
    print("invalid input")
