# Write a program that asks the user to enter a month(in numeric form) a day, and a two-digit year.
# The program should then determine whether the month times the day equals the year.
# If so, it should display a message saying the date is magic. Otherwise,
# it should display a message saying the date is not magic.

# Get the date parameters
month = int(input('Enter the month in number form: '))
day = int(input('Enter the day: '))
year = int(input('Enter the two digit year: '))

if month * day == year:
    print('The date is magic')
else:
    print('The date is not magic')
