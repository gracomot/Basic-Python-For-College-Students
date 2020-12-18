# Assume a speed of 70miles/hr.
# Write a program that displays the distance travelled to three tourist
# attractions given the time it will take to reach the tourist attractions
# Hint:  Distance  =  Speed * Time


# Declare a name constant for speed
SPEED = 70
# Get the travel time(in hrs) to the first toursit attraction
time1 = float(input("Enter the travel time to the first tourist attraction: "))
# Get the travel time (in hrs) to the second tourist attraction
time2 = float(input("Enter the travel time to the second tourist attraction: "))
# Get the travel time (in hrs) to the third tourist attraction
time3 = float(input("Enter the travel time to the third tourist attraction: "))

# Calculate the distance to reach the tourist attractions
distance1 = SPEED * time1
distance2 = SPEED * time2
distance3 = SPEED * time3

# Print the distances
print('The distance it will take to reach tourist attraction 1 is ', format(distance1,'.2f'), 'miles')
print('The distance it will take to reach tourist attraction 2 is ', format(distance2,'.2f'), 'miles')
print('The distance it will take to reach tourist attraction 3 is ', format(distance3,'.2f'), 'miles')


                    
