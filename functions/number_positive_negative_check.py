def check(num):
    if num > 0:
        return("Positive number")
    elif num == 0:
        return("Zero")
    else:
        return("Negative number")


num = float(input("Enter a number: "))

number_check = check(num)
print(number_check)
