# Write a program that asks the user to enter an object's mass,
# then calculates its weight using the formular weight = mass X 9.8
# If the object weighs more than 500 newtons, the program displays
# a message indicating that it is too heavy.
# If the object weights less than 100 newtons, the program display
# a message indicating that it is too light.

# Enter the mass of the object
mass = float(input('Enter the mass of the object: '))
# named constant for gravity
GRAVITY = 9.8
# Compute the weight of the object
weight = mass * GRAVITY
# Determine if the object is too heavy or light
if weight > 500:
    print('The object is too heavy')
if weight < 100:
    print('The object is too light')

