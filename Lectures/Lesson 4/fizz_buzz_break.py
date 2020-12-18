# A program that iterates through integers 1 to the first
# multiple of 3 and 5 and prints "Fizz" for multples of 3,
# "Buzz" for multiples of 5 and "FizzBuzz" for multiples of
# both 3 and 5, other number are printed out

print("Number","\t","Output")
number =  1
while True:
    if (number % 3 == 0 and number % 5 !=0) : # numbers divisible by 3 not by 5
        print(number,"\t","Fizz")
    elif (number % 5 == 0 and number % 3 != 0): # numbers divisible by 5 not by 3
        print(number,"\t","Buzz")
    elif (number % 5 !=0 and number % 3 != 0): # numbers not divisible by 3 and 5
        print(number, "\t",number)
    else:                               # numbers divisible by 3 and 5
        print(number,"\t","FizzBuzz") 
        break
    number+=1

