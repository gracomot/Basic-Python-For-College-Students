# On a roulette wheel, the pockets are numbered from 0 to 36.
# The colors of the pockets are as follows:
# Pocket 0 is green
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black
# For pockets 11 through 18, the odd-numbered pockets are black and the even numbered pockets are red
# For pockets 19 through 28, the odd numbered pockets are red and the even-numbered pockets are black
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red
# Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red or black.
# The program should display an error message if the user enters a number that is outside the range 0 through 36.

# Accept pocket number from user
pkt_num = int(input('Enter a pocket number: '))

# Print a color based on the specified classification 
if pkt_num == 0:
    print('Green')
elif (pkt_num >= 1 and pkt_num <= 10) or (pkt_num >= 19 and pkt_num <= 28):
    if pkt_num % 2 == 1:
        print('Red')
    else:
        print('Black')
elif (pkt_num >= 11 and pkt_num <= 18) or (pkt_num >= 29 and pkt_num <= 36):
    if pkt_num % 2 == 1:
        print('Black')
    else:
        print('Red')
else:
    print('Invalid number')
