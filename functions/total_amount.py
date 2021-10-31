def total_amount(rate,  quantity):
    total_amount = rate * quantity
    return total_amount


def discount_amount(amount, disscount_amount):
    if (amount >= 1000):
        discount_amount = amount * disscount_amount
        return discount_amount


def total_amount_with_discount(amount, discount):
    total_amount_with_discount = amount - discount
    return total_amount_with_discount


def customer_return(customer_note, total_amt_with_discount):
    customer_return = customer_note - total_amt_with_discount
    return customer_return


def message(total_amt_with_discount, customer_note, cust_return):
    if (total_amt_with_discount > customer_note):
        return(f"You don't have enough money. You need {total_amt_with_discount - customer_note} more to pay.")
    else:
        return(f"Your change = {cust_return}")


disscount_amount = 0.1
# read items
item = input("Enter an item: ")
# items rate
rate = int(input("Enter rate: "))
# items quantity
quantity = int(input("Enter an quantity: "))
# customer note
customer_note = int(input("Enter your note: "))


print()
print("----------Bill----------")
print(f"Item = {item}")


amount = total_amount(rate, quantity)
print(f"Total Amount Before Discount = {amount}")

discount = discount_amount(amount, disscount_amount)
print(f"Discount Amount = {discount}")

total_amt_with_discount = total_amount_with_discount(amount, discount)
print(f"Total Amount after discount = {total_amt_with_discount}")

cust_return = customer_return(customer_note, total_amt_with_discount)
print(cust_return)

msg = message(total_amt_with_discount, customer_note, cust_return)
print(msg)
