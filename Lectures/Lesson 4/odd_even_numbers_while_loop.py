# A program that accepts two numbers (lower and upper bound)
# and determines if the numbers between those bounds (inclusive)
# are odd or even numbers

# Accept the lower bound
lower = int(input('Enter the lower bound: '))
# Accept the upper bound
upper = int(input('Enter the upper bound: '))

# print the heading
print('Number','\t','Odd or Even')
# Loop through numbers and determine if odd or even
while lower <= upper:
    if lower%2 == 0:
        print(lower,'\t','Even')
    else:
        print(lower,'\t','Odd')
    lower=lower+1
    
    
