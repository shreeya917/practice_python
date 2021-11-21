def price_categories(vehicle):
    if vehicle == "car":
        return 1000

    elif vehicle == "bike":
        return 500

    elif vehicle == "scooter":
        return 250

    else:
        return 0


vehicle = input("Enter your vehicle: ")
people = int(input("Enter no of peoples: "))

print()
print("----------Bill----------")
print(f"Vehicle = {vehicle}")


if people == 1:
    price = price_categories(vehicle)
    print(f"Your need to pay {price}")

elif people <= 2:
    price = price_categories(vehicle)
    amount = price - 50
    print(f"Your need to pay {amount}")

elif people <= 5:
    price = price_categories(vehicle)
    amount = price - 100
    print(f"Your need to pay {amount}")

else:
    print("Retry!!")
