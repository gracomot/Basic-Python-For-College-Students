# The month of February normally has 28days. But if it is a leap year, February has 29 days.
# Write a program that asks the user to enter a year.
# The program should then display the number of days in February that year.
# Use the following criteria to identify leap year:
# Determine whether the year is divisible by 100.
# If it is, then it is a leap year if and only if it is also divisible by 400.
# For example, 2000 is a leap year, but 2100 is not
# If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4.
# For example 2008 is a leap year, but 2009 is not.

# Get the year from the user
year = int(input('Enter the year: '))
if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
else:
    if year % 4 == 0:
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
