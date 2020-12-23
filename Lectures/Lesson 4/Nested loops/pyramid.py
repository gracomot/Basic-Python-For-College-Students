# A program to draw a pyramid
# Get the height of the pyramid
height = int(input("Enter the height of the pyramid: "))
asterisks = 1
spaces = height
for i in range(1, height+1): # outer loop for the height of the pyramid
    for space in range(1,spaces):# prints the spaces on each row
        print(" ",end="")
    for j in range(1, asterisks+1):# prints the asterisks on each row
        print("*",end="")
    asterisks = asterisks+2 # asterisks increase by 2 on each row
    spaces = spaces - 1 # spaces decrease by 1 on each row
    print()
