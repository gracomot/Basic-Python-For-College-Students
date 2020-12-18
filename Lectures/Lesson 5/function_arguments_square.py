# A Program that shows how an argument can be passed into a function
def square_number(number):
    result = number*number
    print("The square of",number,"is",result)

# Main method calls the square_number function
def main():
    # Get a number from user
    value = int(input("Enter a number: "))
    square_number(value) 
                
# Call the main method
main()
