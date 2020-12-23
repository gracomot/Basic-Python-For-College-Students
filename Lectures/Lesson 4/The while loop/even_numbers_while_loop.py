# A program that takes two numbers as input and prints
# the odd numbers between those two numbers both inclusive
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

if (lower%2 == 0): # lower bound is even, increment by 1
    lower = lower + 1

while (lower <= upper):
    print(lower)
    lower=lower + 2 # lower+=2

              
