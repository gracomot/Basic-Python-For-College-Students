# Question 8 (Leap Year)
# Write a program that takes a year as input and determines if the year
# is a leap year or not. Use the criteria below to identify leap year
#	All years which are perfectly divisible by 4 are leap years except
# for century years (years that end with 00) which is leap year only
# if it is perfectly divisible by 400 e.g 2000 is a leap year but 2100 is not


# Get the year from the user
year = int(input('Enter the year: '))
# Check if it is century year
if year % 100 == 0:
    if year % 400 == 0: # check if the century year us divisible by 400
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
else:
    if year % 4 == 0:
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
