# A program to find the circumference and area of a circle
import math

def main():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    area = math.pi*radius**2
    print("The circumference of a circle with radius",radius,
          "is",format(circumference,'.2f'))
    print("The area of a circle with radius",radius,"is",format(area,'.2f'))

# Call the main function
main()
