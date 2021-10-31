def interest(principal, time, rate):
    simple_interest = principal * rate * time / 100
    return simple_interest


def total_amount(principal, si):
    amount = principal + si
    return amount


principal = int(input("Enter Principal: "))
time = int(input("Enter Time: "))
rate = int(input("Enter Rate: "))

print()
print("----------Calculation----------")
print(f"Principal= {principal}")
print(f" Time = {time}")
print(f" Rate = {rate}")

si = interest(principal, time, rate)
print(f" Simple Interest = {si}")

t_amount = total_amount(principal, si)
print(f" Total Amount = {t_amount}")
