# A program that loops from 1 to 10 and determines
# if number is odd or even numbers
def is_odd(number):
    '''A function that checks if a number is odd'''
    if number%2 == 1:
        return True
    else:
        return False
# print the heading
print('Number','\t','Odd or Even')
# Loop through numbers and determine if odd or even
for num in range(1, 11):
    if is_odd(num):
        print(num,'\t','Odd')
    else:
        print(num,'\t','Even')
    
