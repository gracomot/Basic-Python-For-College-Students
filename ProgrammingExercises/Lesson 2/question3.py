# Given that 0.453592kg makes 1 lb, write a program that asks users
# for a value in kg and then convert it to lbs.

# Ask the user for the weight in lbs
weight_in_kg =  float(input('Enter the weight in kg: '))
# convert the weight to lbs
weight_in_lbs = weight_in_kg/0.453592
# Print the weight in pounds
print(weight_in_kg,'kg is equivalent to',format(weight_in_lbs,'.2f'),'lbs')
