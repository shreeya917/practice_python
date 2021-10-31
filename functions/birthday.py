
def birthday (bd_year , bd_month ,bd_day):

    import datetime
    dt = datetime.datetime.today()
    if(bd_day == dt.day and bd_month == dt.month):
        return 'Happy Birthday'

    elif(bd_day < dt.day and bd_month < dt.month and bd_year <= dt.year):
        return 'See you next year'

    else:
        return 'Happy Birthday in advance'

import datetime
name = input('Enter  Name: ')
print("Please enter your birthday")
bd_year = int(input("Year: "))
bd_month = int(input("Month: "))
bd_day = int(input("Day: "))


print(f"Hello {name}")
bday = birthday (bd_year , bd_month ,bd_day)
print(bday)
