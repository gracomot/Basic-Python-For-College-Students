# A program that asks for the length and width of two rectangles.
# The program tells the user which rectangle has the greater area,
# or if the areas are the same

# Enter the length and width of the first rectangle
length1 = int(input('Enter the length of the first rectangle: '))
width1 =  int(input('Enter the width of the first rectangle: '))
# Compute the area of the first rectangle
area1 = length1*width1

# Enter the length and width of the second rectangle
length2 = int(input('Enter the length of the second rectangle: '))
width2 =  int(input('Enter the width of the second rectangle: '))
# Compute the area of the first rectangle
area2 = length2*width2

# Compare the areas of the first and second rectangles
if(area1 > area2):
    print('The area of the first rectangle is greater')
elif(area2 > area1):
    print('The area of the second rectangle is greater')
else:
    print('The areas of rectangle1 and rectangle2 are the same')
