# A program that uses a value returning function to compute factorial
def factorial(number):
    """This function computes the factorial of its argument"""
    factorial = 1
    for i in range(1, number+1):
        factorial*=i
    return factorial # returns a value back 

def main():
    number = int(input("Enter a number: "))
    print(number,"! is ",factorial(number),sep="")

# Call the main function
main()
