# The Fast Freight Shipping Company charges the following rates
#	Weight of Package				Rate per Pound
#	2 pound or less					$1.50
#	Over 2 pounds but not more than 6 pounds	$3.00
#	Over 6 pounds but not more than 10 pounds	$4.00
#	Over 10 pounds					$4.75
# Write a program that asks the user to enter the weight of a package then
# displays the shipping charges

# Get the weight of the package from the user
weight = float(input('Enter the weight of the item: '))
# Display the shipping charges
if weight <= 2:
    charges =  weight * 1.5
elif weight > 2 and weight < 6:
    charges =  weight * 3
elif weight > 6 and weight < 10:
    charges =  weight * 4
else:
    charges =  weight * 4.75
print("Shipping Charges: $", format(charges, '.2f'), sep='')
