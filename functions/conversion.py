def kg_to_g(kilograms):
    grams = kilograms * 1000
    return grams


def g_to_kg(grams1):
    kilograms1 = grams1 / 1000
    return kilograms1


def m_to_cm(meter):
    centimeter = 100 * meter
    return centimeter


def cm_to_m(cm):
    meter = cm / 100
    return meter


def feet_to_inches(ft):
    inch = ft * 12
    return inch


def inches_to_feet(inches):
    feet = inches / 12
    return feet


def dollar_to_nepalirs(dollar):
    nepali_rs = dollar * 118.41
    return nepali_rs


def nepalirs_dollar(nrs):
    dollar1 = nrs * 0.0084
    return dollar1


def cel_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def fahrenheit_to_cel(f):
    cels = (f - 32) * 5/9
    return cels


def year_to_mnth(year):
    months = year * 12
    return months


def mnth_to_year(month1):
    yrs = month1 / 12
    return yrs


def mnth_to_day(month2):
    days = month2 * 30.417
    return days


def day_to_mnth(day1):
    month3 = day1 / 30.417
    return month3


def day_to_hr(day2):
    hr1 = day2 * 24
    return hr1


def hr_to_day(hr2):
    day3 = hr2 / 24
    return day3


def hr_to_mins(hr3):
    min1 = hr3 * 60
    return min1


def mins_to_hr(min2):
    hr4 = min2 / 60
    return hr4


def hr_to_secs(hr4):
    secs = hr4 * 3600
    return secs


def sec_to_hr(secs):
    hr5 = secs / 3600
    return hr5


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
    14.day to mnth
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
    g = kg_to_g(kilograms)
    print(f" g = {g:.2f}")


elif (conversion_operation == '2'):  # g to kg
    grams1 = float(input("Enter grams:"))
    kg = g_to_kg(grams1)
    print(f" kg  = {kg:.2f}")

elif (conversion_operation == '3'):  # m to cm
    meter = float(input("Enter  meter:"))
    cm = m_to_cm(meter)
    print(f" cm = {cm:.2f}")


elif (conversion_operation == '4'):  # cm to m
    cm = float(input("Enter cm:"))
    m = cm_to_m(cm)
    print(f" m = {m:.2f}")


elif (conversion_operation == '5'):  # feet to inches
    ft = float(input("Enter feet: "))
    inch = feet_to_inches(ft)
    print(f" inches = {inch:.2f}")


elif (conversion_operation == '6'):  # inches to feet
    inches = float(input("Enter inches: "))
    feets = inches_to_feet(inches)
    print(f" feet = {feets:.2f}")

elif (conversion_operation == '7'):  # dollar to nepali rs
    dollar = float(input("Enter dollar: "))
    rs = dollar_to_nepalirs(dollar)
    print(f"Nepali Rs = {rs:.2f}")


elif (conversion_operation == '8'):  # nepali rs to dollar
    nrs = float(input("Enter Nepali Rs: "))
    dollar_1 = nepalirs_dollar(nrs)
    print(f"Dollar = {dollar_1:.2f}")

elif (conversion_operation == '9'):  # cel to fahrenheit
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheits = cel_to_fahrenheit(celsius)
    print(f"Fahrenheit = {fahrenheits:.2f}")

elif (conversion_operation == '10'):  # fahrenheit to cel
    f = float(input("Enter a temperature in Fahrenheit: "))
    cels = fahrenheit_to_cel(f)
    print(f"Celsius = {cels:.2f}")


elif (conversion_operation == '11'):  # year to mnth
    year = float(input("Enter year: "))
    months = year_to_mnth(year)
    print(f"Months= {months:.2f}")


elif (conversion_operation == '12'):  # mnth to year
    month1 = float(input("Enter month: "))
    yrs = mnth_to_year(month1)
    print(f"Year = {yrs:.2f}")


elif (conversion_operation == '13'):  # mnth to day
    month2 = float(input("Enter month: "))
    days = mnth_to_day(month2)
    print(f"Day = {days:.2f}")


elif (conversion_operation == '14'):  # day to mnth
    day1 = float(input("Enter Day: "))
    month_3 = day_to_mnth(day1)
    print(f"Month= {month_3:.2f}")


elif (conversion_operation == '15'):  # day to hr
    day2 = float(input("Enter  Day: "))
    hr_1 = day_to_hr(day2)
    print(f"Hours = {hr_1:.2f}")

elif (conversion_operation == '16'):  # hr to day
    hr2 = float(input("Enter  hour: "))
    day_3 = hr_to_day(hr2)
    print(f"Day = {day_3:.2f}")

elif (conversion_operation == '17'):  # hr to mins
    hr3 = float(input("Enter hour "))
    min_1 = hr_to_mins(hr3)
    print(f"Minutes = {min_1:.2f}")


elif (conversion_operation == '18'):  # mins to hr
    min2 = float(input("Enter minutes: "))
    hr_4 = mins_to_hr(min2)
    print(f"Hours = {hr_4:.2f}")


elif (conversion_operation == '19'):  # hr to secs
    hr4 = float(input("Enter hour: "))
    secss = hr_to_secs(hr4)
    print(f" Seconds = {secss:.2f}")

elif (conversion_operation == '20'):  # secs to hr
    secs = float(input("Enter a month: "))
    hr_5 = sec_to_hr(secs)
    print(f" Hour = {hr_5:.2f}")


elif (conversion_operation == '21'):  # exit
    print("Goodbye")


else:  # invalid
    print("Invalid input!!")
