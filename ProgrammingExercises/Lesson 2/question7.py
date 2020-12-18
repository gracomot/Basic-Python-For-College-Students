# A program that ask a user for the gross pay and
# consider some deductions (as shown below) and displays their value
# before displaying the net pay.
# Federal Tax - 12%
# State Tax - 4%
# Retirement Contribution - 6%

# Ask user for gross pay
gross_pay = float(input("Enter the gross pay: "))
# Calculate deductions
federal_tax = 0.12 * gross_pay
state_tax = 0.04 * gross_pay
retirement = 0.06 * gross_pay

# Calculate net pay
net_pay = gross_pay - (federal_tax + state_tax + retirement)

# Display deductions and net pay
print("Federal Tax: $",format(federal_tax,'.2f'))
print("State Tax: $",format(state_tax,'.2f'))
print("Retirement: $",format(retirement,'.2f'))

# Display net pay
print("Net Pay: $",format(net_pay,'.2f'))

