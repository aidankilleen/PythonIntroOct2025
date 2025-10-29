# datetime_investigation.py

from datetime import date

today = date.today()
print(today)

# object is a core building block
# date is an object
# an object has properties
# a date object has 3 properties - day, month and year
print(today.day)
print(today.month)
print(today.year)

# an object has functions
print (today.weekday())
print (today.strftime("%d/%m/%Y")) # format strings for dates

# dates are not trivial so it's handy to have a class to take care of them

print (f"(c) Professional Training {date.today().year}")



