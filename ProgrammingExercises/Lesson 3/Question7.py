# Question 7 (Time Calculator)
# Write a program that asks the user to enter a time duration in seconds.
# Your program should appropriately convert the duration entered in seconds
# to minutes, hours and days using the guidelines provided below;
#	If the number of seconds entered is greater than or equal to 60,
#       the program should convert the seconds entered to minutes and seconds
#	If the number of seconds entered is greater than or equal to 3600,
#       the program should convert the seconds entered to hours, minutes and seconds
#	If the number of seconds entered is greater than or equal to 86400,
#       the program should convert the seconds entered to days, hours,
#       minutes and seconds

# Declare named constants
MINUTES = 60
HOURS = 3600
DAYS = 86400

# Get the number of seconds from the user
seconds = int(input('Enter the number of seconds: '))

days = seconds//DAYS
hours = (seconds%DAYS) // HOURS
minutes =  (seconds - (days*DAYS + hours*HOURS))// MINUTES
seconds_remaining = seconds - (days*DAYS + hours*HOURS + minutes*MINUTES)

# print message
msg = ""
if days > 0:
    msg+= str(days)+' days '
if hours > 0:
    msg+= str(hours)+' hours '
if minutes > 0:
    msg+= str(minutes)+' minutes '
if seconds_remaining > 0:
    msg+= str(seconds_remaining)+' seconds.'
print(msg)

