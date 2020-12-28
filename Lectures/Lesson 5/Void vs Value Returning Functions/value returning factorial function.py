# A program that uses a value return function to compute factorial
def factorial(number):
    """This function computes the factorial of its number argument"""
    num_factorial = 1
    for i in range(1, number+1):
        num_factorial*=i
    return num_factorial # returns a value back to the calling statement

num = int(input("Enter a number: ")) # Get input from user
# number_factorial = factorial(num) # Get the value returned by factorial function
print(num,"! is ",factorial(num) ,sep="")
