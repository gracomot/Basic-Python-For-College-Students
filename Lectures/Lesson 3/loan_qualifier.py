# A program that determines if a bank customer
# qualifies for a loan based on the customer's
# annual salary and the years worked

# Declare named constants for the parameters required to get a loan
MIN_SALARY = 30000
MIN_YEARS_WORKED = 2
# Get the annual salary and the years worked as input
annual_salary = float(input('Enter the annual salary: '))
years_worked = int(input('Enter the number of years worked: '))

# Check if the customer qualifies for the loan
if annual_salary >= 30000:
    if years_worked >= MIN_YEARS_WORKED:
        print('You qualify for the loan')
    else:
        print('You must have worked for at least 2 years to be approved')
else:
    print('You must have an annual salary of at least $30,000 to be approved')
    


