# Write a program that accepts two floating numbers (a lower bound and an upper bound).
# Your program should random generate a floating number between the two  ranges
# and display the floor and ceiling of the generated floating number
# Format the generated floating point to 2decimal places

import random
import math
def main():
    lower = float(input("Enter the first floating number: "))
    upper= float(input("Enter the second floating number: "))
    # Generate a floating number between lower and upper
    num = random.uniform(lower, upper)
    ceil = math.ceil(num)
    floor = math.floor(num)
    print("The ceiling of",format(num,'.2f'),"is",ceil,"and the floor is",floor)

# Call the main function
main()
    
