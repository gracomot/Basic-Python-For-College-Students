# A Program to demonstrate how None keyword
# can be used to handle exceptions
def divide_numbers(number1, number2):
    if number2 == 0:
        return None
    else:
        return number1/number2
def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number:"))
    quotient = divide_numbers(number1,number2)
    if quotient is None:
        print("You cannot divide a number by zero")
    else:
        print(number1,"divided by",number2,"is",quotient)

# Call the main function
main()
    
