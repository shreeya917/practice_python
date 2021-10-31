def x_midpoint(x1,x2):
    x_midpoint = (x1 + x2)/2
    return x_midpoint

def y_midpoint(y1,y2):
    y_midpoint = (y1 + y2)/2
    return y_midpoint
x1 = float(input("enter x1 : "))
x2 = float(input("enter x2 : "))
y1 = float(input("enter y1 : "))
y2 = float(input("enter y2 : "))

x_point = x_midpoint(x1,x2) 
y_point = y_midpoint(y1,y2)
print(f" Midpoint of(x,y ) is : ({x_point},{y_point})")
