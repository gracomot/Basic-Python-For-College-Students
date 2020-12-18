# A program that determines if a person customer
# qualifies for new credit card based on
# the person's annual salary and the current credit score

# Declare named constants for the parameters required to get a loan
MIN_SALARY = 36000
CREDIT_SCORE_BASELINE = 700
# Get the annual salary and the current credit score as input
annual_salary = float(input('Enter the annual salary: '))
credit_score = int(input('What is your current credit score: '))

# Check if the person qualifies for the credit card
if annual_salary >= MIN_SALARY or credit_score > CREDIT_SCORE_BASELINE:
        print('You qualify for a new credit card')
else:
        print('You do not qualify for a new credit card')

    


