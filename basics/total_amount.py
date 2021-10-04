DISCOUNT_AMOUNT = 0.1

# read items
item = input("Enter an item: ")
# items rate
rate = float(input("Enter rate: "))
# items quantity
quantity = int(input("Enter an quantity: "))
# customer note
customer_note = float(input("Enter your note: "))

# total amount
total_amount = rate * quantity
if (total_amount >= 1000):
    discount_amount = total_amount * DISCOUNT_AMOUNT

total_amount_with_discount = total_amount - discount_amount


customer_return = customer_note - total_amount_with_discount

print()
print("----------Bill----------")
print(f"Item = {item}")
print(f"Total Amount Before Discount = {total_amount}")
print(f"Discount Amount = {discount_amount}")
print(f"Total Amount after discount = {total_amount_with_discount}")

if (total_amount_with_discount > customer_note):
    print(f"You don't have enough money.")
    print(f"You need {total_amount_with_discount - customer_note} more to pay.")

else:
    print(f"Your change = {customer_return}")
