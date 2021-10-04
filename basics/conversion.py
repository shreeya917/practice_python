
print("""
Choose Science operation  you like to perform
    1. kg to g
    2. g to kg
    3. m to cm
    4. cm to m
    5. feet to inches
    6. inches to feet
    7. dollar to nepali rs
    8. nepali rs to dollar
    9. cel to fahrenheit
    10.fahrenheit to cel
    11.year to mnth
    12.mnth to year
    13.mnth to day
    14.day to mth
    15.day to hr
    16.hr to day
    17.hr to mins
    18.mins to hr
    19.hr to secs
    20.secs to hr
    21. Exit
    """)
conversion_operation = input("Enter Option: ")


if (conversion_operation == '1'):  # kg to g
    kilograms = float(input("Enter kilograms:"))
    grams = kilograms * 1000

    print(f" g = {grams:.2f}")


elif (conversion_operation == '2'):  # g to kg
    grams1 = float(input("Enter grams:"))
    kilograms1 = grams1 / 1000

    print(f" kg  = {kilograms1:.2f}")

elif (conversion_operation == '3'):  # m to cm
    meter = float(input("Enter  meter:"))
    centimeter = 100 * meter

    print(f" cm = {centimeter:.2f}")


elif (conversion_operation == '4'):  # cm to m
    cm = float(input("Enter cm:"))
    m = cm / 100

    print(f" m  = {m:.2f}")


elif (conversion_operation == '5'):  # feet to inches
    ft = float(input("Enter feet: "))
    inch = ft * 12

    print(f" inches = {inch:.2f}")


elif (conversion_operation == '6'):  # inches to feet
    inches = float(input("Enter inches: "))
    feet = inches / 12

    print(f" feet = {feet:.2f}")

elif (conversion_operation == '7'):  # dollar to nepali rs
    dollar = float(input("Enter dollar: "))
    nepali_rs = dollar * 118.41

    print(f"Nepali Rs = {nepali_rs:.2f}")


elif (conversion_operation == '8'):  # nepali rs to dollar
    nrs = float(input("Enter Nepali Rs: "))
    dollar1 = nrs * 0.0084

    print(f"Dollar = {dollar1:.2f}")

elif (conversion_operation == '9'):  # cel to fahrenheit
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = (celsius * 1.8) + 32

    print(f"Fahrenheit = {fahrenheit:.2f}")

elif (conversion_operation == '10'):  # fahrenheit to cel
    f = float(input("Enter a temperature in Fahrenheit: "))
    cel = (f - 32) * 5/9

    print(f"Celsius = {cel:.2f}")


elif (conversion_operation == '11'):  # year to mnth
    year = float(input("Enter year: "))
    month = year * 12

    print(f"Months= {month:.2f}")


elif (conversion_operation == '12'):  # mnth to year
    month1 = float(input("Enter month: "))
    yr = month1 / 12

    print(f"Year = {yr:.2f}")


elif (conversion_operation == '13'):  # mnth to day
    month2 = float(input("Enter month: "))
    day = month2 * 30.417

    print(f"Day = {day:.2f}")


elif (conversion_operation == '14'):  # day to mnth
    day1 = float(input("Enter Day: "))
    month3 = day1 / 30.417

    print(f"Month= {month3:.2f}")


elif (conversion_operation == '15'):  # day to hr
    day2 = float(input("Enter  Day: "))
    hr1 = day2 * 24

    print(f"Hours = {hr1:.2f}")

elif (conversion_operation == '16'):  # hr to day
    hr2 = float(input("Enter  hour: "))
    day3 = hr2 / 24

    print(f"Day = {day3:.2f}")

elif (conversion_operation == '17'):  # hr to mins
    hr3 = float(input("Enter hour "))
    min1 = hr3 * 60

    print(f"Minutes = {min1:.2f}")


elif (conversion_operation == '18'):  # mins to hr
    min2 = float(input("Enter minutes: "))
    hr4 = min2 / 60

    print(f"Hours = {hr4:.2f}")


elif (conversion_operation == '19'):  # hr to secs
    hr4 = float(input("Enter hour: "))
    sec = hr4 * 3600

    print(f" Seconds = {sec:.2f}")

elif (conversion_operation == '20'):  # secs to hr
    secs = float(input("Enter a month: "))
    hr5 = secs / 3600

    print(f" Hour = {hr5:.2f}")


elif (conversion_operation == '21'):  # exit
    print("Goodbye")


else:  # invalid
    print("Invalid input!!")
