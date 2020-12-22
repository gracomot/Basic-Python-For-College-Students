# program that asks the user to enter  a person's age.
# The program should display a message indicating whether the person is a Child,
# an Adolescence, an Adult or a Senior Adult.
# Use the age ranges provided below
#	Age 0 - 12 : 		Child
#	Age 13 - 18: 		Adolescent
#	Age 19 - 59: 		Adult
#	Age 60 and above: 	Senior Adult

# Get person's age
age = int(input('Enter your age: '))
# Get the class of person based on age
if age <= 12:
    print('You are a Child')
elif age > 12 and age <=18:
    print('You are an Adolescent')
elif age > 18 and age <=59:
    print('You are an Adult')
else:
    print('You are a Senior Adult')
    
