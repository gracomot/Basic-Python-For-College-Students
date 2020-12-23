# Question 10 (List of Primes)
# Write a program that displays the first n prime numbers in the number system.
# Your input should be a positive integer. e.g if the input is 5, your program
# should display the first 5 prime numbers which are 2, 3, 5, 7, 11.
# Your program should make use of input validation that keeps prompting
# the user to enter a positive integer when the input not a positive integer

# Get an input from the user
nth = int(input("Enter a positive integer: "))
while nth <= 0:
    nth = int(input("Enter a positive integer: "))
    
# Get all prime numbers from 2 upwards
if nth == 1:
    print(2, end =' ')
else:
    print(2,end =' ') # 2 is prime
    count = 1
    number = 3
    while(count < nth):
        is_prime = True
        # Loop from the number to 2 to check for divisibility
        for i in range(number//2,1, -1) :
            if (number%i) == 0:
                is_prime = False
                break
        if is_prime:
            print(number, end =' ')
            count+=1
        number+=1



