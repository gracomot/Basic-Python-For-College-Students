# Write a program that asks a user to enter the  price of items purchased
# from a store, and the percentage of the discount applied, and displays
# the total amount to be paid by the customer assume a tax of 7%

# Get the sales price of the item purchased
sales_price = float(input('Enter the sales price: '))
# Get the discount percentage
discount = float(input('Enter the discount %: '))
# Get the discount value
discount_val = (discount/100) * sales_price
price_after_discount = sales_price - discount_val
# Get the sales tax after discount
sales_tax = 0.07 * price_after_discount
amount_due = price_after_discount +sales_tax
print('The sales price is $', format(sales_price,'.2f'),sep='')
print('The discount price is $', format(discount_val,'.2f'),sep='')
print('The sales tax is after discount $', format(sales_tax,'.2f'),sep='')
print('The amount due is is $', format(amount_due,'.2f'),sep='')


