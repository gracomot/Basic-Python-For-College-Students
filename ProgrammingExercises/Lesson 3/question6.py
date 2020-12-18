# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.
# Write a program that calculates the number of packages of hot dogs and the number
# of packages of hot dog buns needed for a cookout,with the minimum amount of leftovers.
# The program should ask the user for the number of people attending the cookout
# and the number of hot dogs each person will be given.
# The program should display the following details:
# The minimum number of packages of hot dogs required
# The minimum number of packages of hot dog buns required
# The number of hot dog that will be left over
# The number of hot dog buns that will be left over

# Create a named constant for the number of hot dogs and hot dog buns in a package
HOT_DOG_PKG = 10
HOT_DOG_BUNS = 8

# Get the number of people attending the cookout
number_of_people = int(input('How many people will be attending the cookout? '))
ration_per_person = int(input('How many hot dogs will each person be given? '))

# Compute the packages of hot dogs needed
hot_dogs_needed = number_of_people * ration_per_person
hot_dog_pkg_needed = hot_dogs_needed // HOT_DOG_PKG
if hot_dogs_needed % HOT_DOG_PKG != 0:
    hot_dog_pkg_needed = hot_dog_pkg_needed + 1

# Compute the packages of hot dog buns needed
hot_dog_bun_pkg_needed = hot_dogs_needed // HOT_DOG_BUNS
if hot_dogs_needed % HOT_DOG_BUNS  != 0:
    hot_dog_bun_pkg_needed = hot_dog_bun_pkg_needed + 1

# Get the number of left over
hot_dog_leftover = (hot_dog_pkg_needed * HOT_DOG_PKG) - hot_dogs_needed
hot_dog_bun_leftover = (hot_dog_bun_pkg_needed * HOT_DOG_BUNS) - hot_dogs_needed
    
# Print the needed information
print('The minimum number of packages of hot dogs required is ', hot_dog_pkg_needed) 
print('The minimum number of packages of hot dogs buns required is ', hot_dog_bun_pkg_needed)
print('The number of hot dog that will be left over is ',hot_dog_leftover)
print('The number of hot dog buns that will be left over is ', hot_dog_bun_leftover)
