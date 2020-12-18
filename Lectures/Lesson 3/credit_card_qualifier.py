# A program that determines if a customer
# qualifies for new credit card based on
# the person's annual salary and the current credit score

# Declare named constants for the parameters required to get a loan
MIN_SALARY = 36000
CREDIT_SCORE_BASELINE = 700
# Get the annual salary and the current credit score as input
annual_salary = float(input('Enter the annual salary: '))
if(annual_salary >= MIN_SALARY): 
    credit_score = int(input('What is your current credit score: '))

# Check if the person qualifies for the credit card
if annual_salary >= MIN_SALARY:
    if credit_score > CREDIT_SCORE_BASELINE:
        print('You qualify for the credit card')
    else:
        print('Your credit score must be greater than 700 to be approved')
else:
    print('You must have an annual salary of at least $36,000 to be approved')
    


