# Question 7 (Decimal to Binary)
# Write a program that asks a user to enter a number and then prints
# the binary equivalent of the number.

num = int(input("Enter a number: "))
rem_str = ""
number = num
while number >0:
    rem = number % 2
    number = number//2
    # join the remainder as string
    rem_str+=str(rem) 

# reverse rem_str
n = len(rem_str)
ret_str = ""
for i in range(n-1, -1, -1):
    ret_str+=  rem_str[i]

print("The binary equivalent of",num, "is",ret_str)
