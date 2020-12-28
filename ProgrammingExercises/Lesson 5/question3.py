# Write a program that generates a random number between 1 and 100 and prints a
# message specifying if the generated number is odd, even or prime.
# If a number is prime, your program should solely consider it as prime, not odd.
# A sample output is “19 is a prime number” assuming 19 is the generated number

import random

def isOdd(number):
    """A function that determines if a number is odd"""
    return number%2 == 1

def isEven(number):
    """A function that determines if a number is even"""
    return number%2 == 0

def isPrime(number):
    """A function that determines if a number is prime"""
    is_prime = True
    if number == 1:
        is_prime = False
    if number == 2:
        is_prime = True
    for i in range(number//2,1, -1): # A number can only be divisible by at most its half
        if (number%i) == 0:
            is_prime = False
            break
    return is_prime
def main():
    # Generate a random number
    num = random.randint(1,100)
    if isPrime(num):
        print(num, "is a prime number")
    elif isEven(num):
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
    
    

main()
