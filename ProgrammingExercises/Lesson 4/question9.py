# Question 9 (Fibonacci Sequence)
# The Fibonacci sequence is one of the most famous formulas in mathematics.
# Each number in the sequence is the sum of the two numbers that precede it.
# So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
# Write a program that asks for a number n greater than 2.
# Your program should print the fibonacci series up to the nth term.
# E.g if n is 8, your program will displat the fibonacci series up to the
# 8th term and the output should will be 0, 1, 1, 2, 3, 5, 8, 13. Your program should
# make use of input validation that keeps prompting the user to enter a number
# greater than 2 when input is not greate than 2 or is invalid

# Get the a number from the user
nth_term = int(input("Enter a number greater than 2: "))

# Validate the input
while nth_term <= 2:
    nth_term = int(input("Enter a number greater than 2: "))
    
print("The fibonacci series up to the ",nth_term,"th term is", sep='')
prev = 0
current = 1
print(prev,current, end = ' ')
count = 2
while (count < nth_term):
    count+=1
    cumm = prev + current
    print(cumm,end=' ')
    prev = current
    current = cumm
    





    
