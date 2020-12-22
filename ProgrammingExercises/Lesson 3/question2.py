# Question 2 (Areas of Circles)
# The area of a circle is the product of pi and the square of the
# circle’s radius. Write a program that asks for the radius of two circles.
# The program should tell the user which circle has the greater area or if
# the areas are the same.

PI = 3.142

# Enter the radius of the first circle
radius1 = int(input('Enter the radius of the first circle: '))

# Compute the area of the first circle
area1 = PI*radius1**2

# Enter the radius of the second circle
radius2 = int(input('Enter the radius of the second circle: '))

# Compute the area of the first circle
area2 = PI*radius2**2

print("Circle 1 area: ",area1)
print("Circle 2 area: ",area2)

# Compare the areas of the first and second rectangles
if(area1 > area2):
    print('The area of the first circle is greater')
elif(area2 > area1):
    print('The area of the second circle is greater')
else:
    print('The areas of first circle and second circle are the same')
