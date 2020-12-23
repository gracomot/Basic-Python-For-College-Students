# A program to show infinite loop
# This program is meant to print numbers
# from 1 to a specified positive number

# Accept a positive number
number = int(input('Enter a positive number: '))
count = 1
while count <= number:
    print(count)
    count+=1
