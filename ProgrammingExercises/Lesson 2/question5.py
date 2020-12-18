# Write a program that calculates the total price of items purchased
# by customers. Due to the nature of the items sold in the store,
# it is certain that customers will purchase 3 items any time they
# visit the store. Your program should ask for the price of each item,
# calculate the sales tax (4%) and the total amount due.

# Ask user for the price of item 1
price1 = float(input('Enter the price of the first item: '))
# Ask user for the price of item 2
price2 = float(input('Enter the price of the second item: '))
# Ask user for the price of item 3
price3 = float(input('Enter the price of the third item: '))

# Calculate total price
total_price = price1 + price2 + price3

# Calculate sales tax
sales_tax = total_price * 0.04

# Calculate amount due
amount_due = total_price - sales_tax

# print total price, sales price and the amount due
print("Total price: $",format(total_price,',.2f'), sep='')
print("Sales tax: $",format(sales_tax,',.2f'), sep='')
print("Amount due: $",format(amount_due,',.2f'), sep='')
