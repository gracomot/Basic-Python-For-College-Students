# Write a program that accepts two positive integers (a lower bound and an upper bound).
# Your program should loop from the lower bound to the upper bound and display in a tabular
# fashion if the number between both bounds(inclusive)is odd, even or prime. 

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
    # Get two numbers as input
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))
    # Print Heading
    print("Number \t Type")
    for num in range(lower, upper+1):
        if isPrime(num):
            print(num,"\t Prime")
        elif isEven(num):
            print(num, "\t Even")
        else:
            print(num, "\t Odd")
            
# Call the main function
main()
