# A program to compute the hypotenuse of a right triangle
import math
def main():
    # Take the input to the othe other sides of the triangle
    side_a = float(input("Enter the length of the first side: "))
    side_b = float(input("Enter the length of the second side: "))
    hypotenuse = math.hypot(side_a, side_b)# math.sqrt(side_a**2 + side_b**2)
    print("The hypotenuse of a triangle with sides of length",
          side_a,"and",side_b, "is",hypotenuse)

# Call the main function
main()

