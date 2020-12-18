# A program that generates n random numbers
# in the range 1 to 10
import random

def main():
    count = int(input("How many random numbers do you want to generate? "))
    for i in range(count):
        print(random.randint(1,100))
        
# Call the main function
main()
