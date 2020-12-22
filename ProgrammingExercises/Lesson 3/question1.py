# Question 1 (Months in a year)
# Write a program that asks the user for a number in the range 1 through 12.
# The program should display the corresponding month of the year,
# where 1 = January, 2 = February, 3 = March,........11 = November
# and 12 = December. The program should display an error message if the user
# enters a number that is outside the range 1 through 12.

number =  int(input('Enter a number between 1 and 12: '))
# Get the day of week
if (number == 1):
    print('January')
elif (number == 2):
    print('February')
elif(number == 3):
    print('March')
elif(number == 4):
    print('April')
elif(number == 5):
    print('May')
elif(number == 6):
    print('June')
elif(number == 7):
    print('July')
elif (number == 8):
    print('August')
elif(number == 9):
    print('September')
elif(number == 10):
    print('October')
elif(number == 11):
    print('November')
elif(number == 12):
    print('December')
else:
    print('Invalid number')

