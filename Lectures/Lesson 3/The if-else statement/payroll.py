# A program that calculates the gross pay of hourly employees
# An employee is entitled to an overtime which is 1.5 times
# the normal pay rate. The overtime is applicable to additional
# hours above 40

# Declare named constants for overtime rate and base hours
BASE_HOUR =  40
OVERTIME_RATE = 1.25

# Accept pay rate and hours worked as input
hours_worked = float(input("Enter the hours worked: "))
pay_rate = float(input("Enter the pay rate: "))

# check if hours worked is more than 40
if hours_worked > BASE_HOUR:
    # compute overtime hours
    overtime_hours =  hours_worked - BASE_HOUR
    overtime_pay = (overtime_hours*OVERTIME_RATE*pay_rate)
    # compute gross pay with overtime pay in consideration
    gross_pay = (BASE_HOUR * pay_rate) + overtime_pay
else:
    # compute gross pay without overtime
    gross_pay = BASE_HOUR * pay_rate

print("The gross pay is $",format(gross_pay,',.2f'),sep='')
    
