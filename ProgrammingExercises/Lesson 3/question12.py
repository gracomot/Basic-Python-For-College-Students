# Write a program that asks the user to enter a number of seconds and works as follows:
# There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60
# the program should convert the number of seconds to minutes and seconds
# There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600
# the program should convert the number of seconds to hours, minutes and seconds
# There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400
# the program should convert the number of seconds to days, hours, minutes and seconds.

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
