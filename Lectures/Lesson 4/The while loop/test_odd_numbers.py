# A program that takes two numbers as input and prints
# the odd numbers between those two numbers both inclusive
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

while (lower <= upper):
    if (lower % 2 == 1):
        print(lower)
    lower+=1
