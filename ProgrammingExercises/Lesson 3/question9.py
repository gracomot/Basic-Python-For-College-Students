# A Software company sells a package that retails for $99.
# Quantity discounts are given according to the following table:
#		Quantity 		Discount
#		10-19			10%
#		20-49			20%
#		50-99			30%
#		100 or more		40%
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount(if any)
# and the total amount of the purchase after discount

# Declare a named constant for the package price
PKG_PRICE = 99
# Get the number of packages purchased
qty = int(input('Get the number of packages purchased: '))
price_before_discount = PKG_PRICE*qty
if qty >= 10 and qty <= 19:
    purchase = price_before_discount  - (price_before_discount* 0.10)
elif qty >= 20 and qty <= 49:
    purchase = price_before_discount - (price_before_discount * 0.20)
elif qty >= 50 and qty <= 99:
    purchase = price_before_discount - (price_before_discount * 0.30)
else:
    purchase = price_before_discount - (price_before_discount * 0.40)

print('The total amount of your purhase after discount is: ',format(purchase,'.2f'))
