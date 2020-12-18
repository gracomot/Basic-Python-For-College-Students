# A program that takes a number as input and returns
# the factorial of the number

number = int(input("Enter a positive number: ")) # Get the input
factorial = 1 # initialize factorial accumulator

# Find the factorial by accumlating the
# product of numbers from 1 to the specified number
for i in range(1, number+1):
    factorial *= i # factorial = factorial * i
    
# Display the factorial
print(number,'! is ',factorial, sep='')
