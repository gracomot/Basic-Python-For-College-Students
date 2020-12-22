# Question 5 (Income Group)
# Write a program that asks the user to enter their annual income.
# The program should display a message indicating whether the person
# is a low income earner, middle income earner or high income earner.
# Use the income bracket provided below;
#	Income less than $40,100:		Low Income Earner
#	Income between $40,100 and $120,400: 	Middle Income Earner
#	Income greater than $120,400:		High Income Earner

# Get the annual income 
income = int(input('Enter your annual income: '))
if income < 40100:
    print("You are a low income earner")
elif income >= 40100 and income <= 120400:
    print("You are a middle income earner")
else:
    print("You are a high income earner")
