# A program that iterates through integers 1 to 30
# and prints "Fizz" for multples of 3,
# "Buzz" for multiples of 5 and "FizzBuzz" for multiples of
# both 3 and 5, other numbers are skipped

print("Number","\t","Output")
number =  0
while number < 30:
    number+=1
    if (number % 3 == 0 and number % 5 !=0) : # divisible by 3 not by 5
        print(number,"\t","Fizz")
    elif (number % 5 == 0 and number % 3 != 0):# divisible by 5 not by 3
        print(number,"\t","Buzz")
    elif (number % 5 ==0 and number % 3 == 0):# divisible by 3 and 5
        print(number,"\t","FizzBuzz")
    else:
        continue
        
    

