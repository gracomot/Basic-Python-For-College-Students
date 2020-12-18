# A program that genrates two random numbers
# and finds their sum
import random

def main():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    sum = number1 + number2
    print("The sum of",number1,"and",number2,"is",sum)
    
# Call the main function
main()
