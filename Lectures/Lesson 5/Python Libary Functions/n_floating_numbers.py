# Write a program to display n random floating point numbers
import random
def main():
    n = int(input("How many numbers do you want? "))
    for i in range(n):
            print(random.random())
            
# Call the main function
main()
