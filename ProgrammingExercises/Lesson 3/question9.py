# Question 9 (Coins to Bill)
# You were consulted to write a coin to bill conversion program for a coin
# machine. Your program should ask for the number of quarters, dimes, nickels and pennies and should display the dollar and cent amount the user gets. Use the information below for the conversion
#	1 quarter - 25cents
#	1 dime - 10cents
#       1 nickels - 5cents
#       1 penny - 1 cent
#   100 cents - 1 dollar
# For example, 20 quarters, 8 dimes, 16 nickels and 5 penny should give $6.65

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
dollars = cents//100
cents_rem = cents%100
print("The coin machine will give you back $",dollars,".",cents_rem, sep='')
