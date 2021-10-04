
import datetime
name = input('Enter  Name: ')
print("Please enter your birthday")
bd_year = int(input("Year: "))
bd_month = int(input("Month: "))
bd_day = int(input("Day: "))

dt = datetime.datetime.today()

print(f"Hello {name}")

if(bd_day == dt.day and bd_month == dt.month):
    print("Happy Birthday")

elif(bd_day < dt.day and bd_month < dt.month and bd_year <= dt.year):
    print(" See you next year")

else:
    print("Happy Birthday in advance")
