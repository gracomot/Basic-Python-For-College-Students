# Create a change-counting game that tells the user to enter the number of
# coins required to make exactly one dollar. The program should prompt the user
# to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar,
# the program should congratulate the user for winning the game.
# Otherwise, the program should display a message indicating whether
# the amount entered was more than or less than one dollar.

# Create named constants for all coin values
PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25

# Get the number of coins from user
pennies =  int(input('How many pennies do you have? '))
nickels =  int(input('How many nickels do you have? '))
dimes =  int(input('How many dimes do you have? '))
quarters =  int(input('How many quarters do you have? '))

# Sum up all the coins
cents = (pennies*PENNY) + (nickels*NICKEL) + (dimes*DIME) + (quarters*QUARTER)
# 100 cents makes one dollar
if cents == 100:
    print('Congratulations you won the game')
elif cents < 100:
    print('The amount you entered is less than a dollar')
else:
    print('The amount you entered is greater than a dollar')
