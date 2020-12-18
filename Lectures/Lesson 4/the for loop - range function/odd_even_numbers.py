# A program that accepts two numbers (lower and upper bound)
# and determines if the numbers between those bounds (inclusive)
# are odd or even number

# Accept the lower bound
lower_bound = int(input('Enter the lower bound: '))
# Accept the upper bound
upper_bound = int(input('Enter the upper bound: '))

# print the heading
print('Number','\t','Odd or Even')
# Loop through numbers and determine if odd or even
for num in range(lower_bound, upper_bound+1):
    if num%2 == 0:
        print(num,'\t','Even')
    else:
        print(num,'\t','Odd')
    
    
