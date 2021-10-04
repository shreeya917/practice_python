principal = float(input("Enter Principal: "))
time = float(input("Enter Time: "))
rate = int(input("Enter Rate: "))

simple_interest = principal * rate * time / 100


total_amount = principal + simple_interest

print()
print("----------Calculation----------")
print(f"Principal= {principal}")
print(f" Time = {time}")
print(f" Rate = {rate}")
print(f" Simple Interest = {simple_interest}")
print(f" Total Amount = {total_amount}")
