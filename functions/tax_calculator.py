def tax_calculator(salary):

    if (salary <= 10000):  # 1per tax
        tax_amount = salary*0.01
        return tax_amount

    elif (salary <= 30000):  # 2 per tax
        tax_amount = salary*0.02
        return tax_amount

    elif (salary <= 50000):  # 3 per tax
        tax_amount = salary*0.03
        return tax_amount
    else:                   # 5 per tax
        tax_amount = salary*0.05
        return tax_amount


salary = float(input("Enter your salary: "))
tax_amount = 0

calculator = tax_calculator(salary)
print(calculator)
