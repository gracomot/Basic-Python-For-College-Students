# program that asks the user to enter  a person's age.
# The program should display a message indicating whether the person
# is an infant, a child, a teenager, or an adult.
# The guidelines for the classification are below;
# If the person is 1year old or less, he or she is an infant
# If the person is older than 1year, but younger than 13years, he or she is a child
# If the person is at least 13years old, but less than 20years old, he or she is a teenager
# If the person is at least 20years old, he or she is an adult

# Get person's age
age = int(input('Enter your age: '))
# Get the class of person based on age
if age <= 1:
    print('You are an Infant')
elif age > 1 and age < 13:
    print('You are a Child')
elif age >=13 and age < 20:
    print('You are a Teenager')
else:
    print('You are an Adult')
    
