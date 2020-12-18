# A program that asks the user for a number in the range of 1 through 7.
# and displays the corresponding day of the week where 1 = Monday,
# 2 =  Tuesday,  3 =  Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday,
# and 7 = Sunday. The program should displays an error message if the user
# enters a number that is outside the range 1 through 7.

number =  int(input('Enter a number: '))
# Get the day of week
if (number == 1):
    print('Monday')
elif (number == 2):
    print('Tuesday')
elif(number == 3):
    print('Wednesday')
elif(number == 4):
    print('Thursday')
elif(number == 5):
    print('Friday')
elif(number == 6):
    print('Saturday')
elif(number == 7):
    print('Sunday')
else:
    print('Invalid number')

