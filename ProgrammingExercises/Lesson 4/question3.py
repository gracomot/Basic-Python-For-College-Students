# Question 3 (Draw a Triangle)
# Write a program that draws a triangle. Your program should ask for the height
# of the triangle and it should display a triangle with the specified height.

# Get the height of triangle as input
height = int(input("Enter the height of the triangle: "))
for i in range(1, height+1):
    for j in range(i):
        print("*",end='')
    print()
