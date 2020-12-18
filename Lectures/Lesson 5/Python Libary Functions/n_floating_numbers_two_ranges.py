# Write a program to display n random floating point numbers
# between two numbers
import random
def main():
    n = int(input("How many numbers do you want? "))
    start_val = float(input("Enter a starting value: "))
    end_val = float(input("Enter an ending value: "))
    for i in range(n):
            print(random.uniform(start_val,end_val))
            
# Call the main function
main()
