# Question 6 (Prime Number)
# A prime number is a number that is divisible by itself and 1.
# Write a program that takes a number from a user and tells whether
# the number is prime or not.
# Note: 1 is not a prime number but 2 is a prime number

is_prime = True
# Get the number as input from the user
number = int(input("Enter a number: "))
if number == 2:
    print(number,"is prime")

elif number == 1:
    print(number,"is not prime")

else:
    # Loop from the number to 2 to check for factors
    for i in range(number//2,1, -1): # A number can only be divisible by at most its half
        if (number%i) == 0:
            is_prime = False
            break
    if is_prime:
        print(number,"is prime")
    else:
        print(number,"is not prime")
