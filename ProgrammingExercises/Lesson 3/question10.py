# Question 10 (Shipping Charges)
# An online store charges for shipping based on the weight of the item purchased. Write a program that takes the weight of the items purchased and calculates the shipping cost. Use the information for your calculations
#	5lbs or less 					$4.00
#       Over 5 pounds but not more than 10lbs	        $5.50
#       Over 10lbs but not more than 20lbs		$7.00
#       Over 20lbs 					$9.00			$9.00

# Create named constant for shipping charges
FIVE_OR_LESS = 4
OVER_FIVE_LESS_THAN_TEN = 5.50
OVER_10_LESS_THAN_20 = 7.00
OVER_20 = 9.00

# Get the weight of the package from the user
weight = float(input('Enter the weight of the item: '))
# Display the shipping charges
if weight <= 5:
    charges =   FIVE_OR_LESS
elif weight > 5 and weight < 10:
    charges =  OVER_FIVE_LESS_THAN_TEN
elif weight > 10 and weight < 20:
    charges =  OVER_10_LESS_THAN_20
else:
    charges = OVER_20
print("Shipping Charges: $", format(charges, '.2f'), sep='')
