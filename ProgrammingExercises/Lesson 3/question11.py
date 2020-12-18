# Write a program that calculates and displays a person's body mass index (BMI).
# The BMI is often used to determine whether a person is overweight or underweight
# for his or her height. A person's BMI is calculated with the following formula:
#		BMI = weight x 703/height^2	
# where weight is measured in pounds and height is measured in inches.
# The program should ask the user to enter his or her weight and height,
# then display the user's BMI. The program should also display a message
# indicating whether the person has optimal weight, is underweight, or is overweight.
# A person's weight is considered to be optimal if his or her BMI is between 18.5 and 25.
# If the BMI is less than 18.5, the person is considered to be underweight.
# If the BMI is greater than 25, the person is considered to be overweight.

# Get the user's weight and height
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))
# Compute the BMI
BMI = weight *(703/(height**2))
# Display a message to the user
if BMI >= 18.5 and BMI <= 25:
    print('You weight is optimal')
elif BMI < 18.5:
    print('You are underweighed')
else:
    print('You are overweighed')
