# Combinations are a way to calculate the total outcomes of an event where
# order of the outcomes does not matter. To calculate combinations, we will
# use the formula nCr = n! / r! * (n - r)!, where n represents the number of
# items, and r represents the number of items being chosen at a time.
# Write a program that asks for the value of n(number of items) and
# r(number of items of interest) and displays the value of nCr.

def factorial(number):
    factorial = 1
    # Find the factorial by accumlating the
    # product of numbers from 1 to the specified number
    for i in range(1, number+1):
        factorial *= i # factorial = factorial * i
    return factorial

def combination(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def main():
    n = int(input("Enter the value of n (number of items): "))
    r = int(input("Enter the value of r (number of items of interest): "))
    comb = combination(n, r)
    print(n,"C",r," is ", comb, sep='')

# Call the main function
main()

