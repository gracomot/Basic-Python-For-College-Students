# Adisa purchased some stock from XYZ communication company.
# Find the details of the purchase below;

# The number of shares that Adisa purchase was 2,800.
# When Adisa purchased the stock, he paid $23.25 per share.
# Adisa paid his stockbroker a commission that amounted to 4%
# of the amount he paid for the stock

# Two weeks later, Adisa sold the stock. Here are the details of the sale:
# The number of shares that Adisa sold was 2,800.
# He sold the stock for $27.50 per share.
# He paid his stockbroker another commission that amounted to 4% of
# the amount he received for the stock

# Write a program that displays the following information

# The amount of money Adisa paid for the stock.
# The amount of commission Adisa paid his broker when he bought the stock.
# The amount for which Adisa sold the stock.
# The amount of commission Adisa paid his broker when he sold the stock.
# Display the amount of money that Adisa had left when he sold the stock
# and paid his broker (both times). 


# Create a named constant for the stock purchased by Adisa
STOCK =  2800
# Get the amount of money Adisa paid for the stock
amount_paid = STOCK * 23.25
# Get the amount of money Adisa paid  the stockbroker when he bought the stock
commission_at_stock_purchase = 0.04 *  amount_paid
# Get the amount of money Adisa sold the stock
amount_sold = STOCK * 27.50
# Get the amount of money Adisa paid  the stockbroker when he sold the stock
commission_at_stock_sales = 0.04 * amount_sold
# Get the amount remaining after he sold the stock and paid the stockbroker
amount_left = (amount_sold - commission_at_stock_sales) -(amount_paid + commission_at_stock_purchase)

print('The amount Adisa paid for the stock he bought: $', format(amount_paid, '.2f'), sep='')
print('The amount Adisa paid the stockbroker when he bought the stock: $', format(commission_at_stock_purchase, ',.2f'), sep='')
print('The amount Adisa sold the stock: $', format(amount_sold, '.2f'), sep='')
print('The amount Adisa paid the stockbroker when he sold the stock: $', format(commission_at_stock_sales, ',.2f'), sep='')
print('The anount Adisa has left when he sold the stock and paid the broker: $',format(amount_left,',.2f'), sep='')

