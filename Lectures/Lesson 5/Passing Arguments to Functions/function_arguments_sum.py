# A program that shows how to pass multiple arguments to a function
# Finds the sum of two numbers

# A function that finds the sum of two numbers
def sum_numbers(number1, number2):
    return number1+number2

def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    sum = sum_numbers(number1, number2)
    print("The sum of",number1,"and",number2,sum)

# Call the main function
main()
