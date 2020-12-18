# Write a program that asks the user to enter
# the projected annual tuition made from enrollment, then displays
# the profit that will be made from that amount.
# Assume profit is 35% of total tuition

# Ask the user for projected annual tuition
total_tuition = float(input('Enter the projected annual tuition: '))
# Calculate the profit
profit = 0.38 * total_tuition
# Display the profit in the format $9,999,999.99
print('The profit is $', format(profit,',.2f'), sep='')

