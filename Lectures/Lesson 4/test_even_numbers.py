# A program that takes two numbers as input and prints
# the even numbers between those two numbers both inclusive
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

while (lower <= upper):
    if (lower % 2 == 0):
        print(lower)
    lower+=1
