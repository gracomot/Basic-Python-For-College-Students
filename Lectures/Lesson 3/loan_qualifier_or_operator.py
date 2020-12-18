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
if annual_salary >= MIN_SALARY or years_worked >= MIN_YEARS_WORKED:
    print('You qualify for the loan')
else:
    print('You do not qualify for the loan')    


