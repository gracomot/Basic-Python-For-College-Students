# A Jollof rice recipe uses the following major ingredients;
# 2 cups of rice
# 8 cups of water
# 0.5 cup of oil
# 1 cup of chicken broth
# This recipe is just for 5 plates of jolleof rice.
# Write a program that asks the user how many plates of jollof rice he or she wants to make,
# then displays the proportion of ingeredients needed for the specified plates of Jollof rice

# Get the number of plate to be prepared
plates_needed = int(input('Enter the number of plates you would like to prepare : '))

# Create a named constant for the standard jollof rice recipe
PLATES = 5

# Get the cups of rice needed
rice = plates_needed/PLATES * 2
# Get the cups of water needed
water = plates_needed/PLATES * 8
# Get the cups of oil needed
oil = plates_needed/PLATES * 0.5
# Get the cups of water needed
broth = plates_needed/PLATES * 1

# Print the cups of ingredients needed
print(format(rice,'.2f'),'cups of rice, ', format(water,'.2f'),'cups of water, ',format(oil,'.2f'),'cups of oil, ',format(broth,'.2f'),'cups of chicken broth')

