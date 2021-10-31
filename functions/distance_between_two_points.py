
def distance_btwn_points(x1, x2, y1, y2):
    distance = ((((x2 - x1)**2) + ((y2-y1)**2))**0.5)
    return distance


x1 = float(input("enter x1 : "))
x2 = float(input("enter x2 : "))
y1 = float(input("enter y1 : "))
y2 = float(input("enter y2 : "))

distance_points = distance_btwn_points(x1, x2, x2, y2)

print(f"Distance between (x1,x2) and (y1,y2) is : {distance_points}")
