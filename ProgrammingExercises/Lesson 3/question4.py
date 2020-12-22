# Question 4 (Distance Calculator)
# Write a program that takes the speed (miles/hr) at which a traveller is
# traveling and the time (hr) a journey takes. Use the formula
#	distance = speed * time
# Your program should find the distance travelled. If the distance is greater
# than 100miles, display a message indicating that the journey is a long one.
# If the distance travelled is less than 100miles, display a message
# indicating that the journey is a short one.

# Enter the mass of the object
speed = float(input('Enter the speed travelled in miles/hr: '))
time = float(input('Enter the time travelled in hr: '))
distance =  speed * time
print("The distance travelleed is", distance, "miles")
# Determine if journey is long or short
if distance > 100:
    print('The journey is long')
else:
    print('The journey is short')

