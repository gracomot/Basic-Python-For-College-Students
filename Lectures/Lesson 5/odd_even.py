# A Program that accepts two numbers and determines if the numbers
# between the two numbers are odd of even

def odd_even(number):
    if number % 2 == 0:
        return "Odd"
    else:
        return "Even"
def display_table(lower, upper):
    for number in range(lower, upper+1):
        print(number, "\t", odd_even(number))
    
# The main function
def main():
    # Accept lower bound and upper bound
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter a higher bound: "))
    # print Header
    print("Number \t Odd or Even")
    # call the display_table function
    display_table(lower, upper)

# Call the main function
main()
    
