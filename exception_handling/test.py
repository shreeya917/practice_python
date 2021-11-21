

try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    divide = num2 / num1
    print(divide)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
except Exception:
    print("An error occured.")
# finally:
#     print("finally")
