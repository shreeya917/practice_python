def swap_x(x, y,):
    temp = x
    x = y
    return x


def swap_y(x, y,):
    temp = x
    y = temp
    return y


x = input('Enter value of x: ')
y = input('Enter value of y: ')

swap = swap_x(x, y)
print(swap)

swapp = swap_y(x, y)
print(swapp)
