salary =float(input("Enter your salary: "))
tax_amount = 0

if (salary <= 10000): # 1per tax
    tax_amount = salary*0.01


elif (salary <= 30000): # 2 per tax
    tax_amount = salary*0.02

elif (salary <= 50000): # 3 per tax
    tax_amount = salary*0.03

else:                   # 5 per tax
    tax_amount = salary*0.05 

print(f"tax amount = {tax_amount}")