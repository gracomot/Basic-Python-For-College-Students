# A program to compute the gross pay of an hourly employee

# Input the hours worked
hours_worked = float(input('Enter the hours worked: '))

# Input the hourly pay rate
pay_rate = float(input('Enter the pay rate: '))

# Calculate the gross pay as hours worked multiplied by pay rate
gross_pay = hours_worked * pay_rate

# Display the gross pay
print('Gross Pay: $', format(gross_pay, ',.2f'), sep = '')
