# Given the quadratic equation ax^2 + bx + c
# Where, a, b, and c are coefficient and real numbers and also a ≠ 0. 
# Write a program that accepts the coefficients (a, b and c) of a quadratic
# equation and returns the roots of the equation.
# Hint: Write a helper function that finds the discriminant (b^2 - 4ac) of the equation.
# Use the following hints from the discriminant to determine if the equation has valid roots;
# If the discriminant is > 0, the roots are real and different
# If the discriminant is = 0, the roots are real and the same
# If the discriminant is < 0, the roots are complex.
# If the roots of the equation whose coefficient is entered are not real numbers,
# your program should display the message “The roots are complex”.

import math
def discriminant(a, b , c):
    return b**2 - (4*a*c)

def main():
    # Get the coefficients of the equation
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    disc = discriminant(a, b, c)
    if disc > 0:
        root1 = (-b + math.sqrt(disc))/2*a
        root2 = (-b - math.sqrt(disc))/2*a
        print("The roots are",root1, "and",root2)
    elif disc == 0:
        root = -b/(2*a)
        print("The roots are the same and has a value of",root)
    else:
        print("The roots are complex")
        
# Call the main function
main()
