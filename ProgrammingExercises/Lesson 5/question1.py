# The hexadecimal system (shortly hex), uses the number 16 as its base (radix).
# As a base-16 numeral system, it uses 16 symbols. These are the 10 decimal digits
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and the first six letters of the English alphabet
# (A, B, C, D, E, F). The letters are used because of the need to represent the values
# 10, 11, 12, 13, 14 and 15 each in one single symbol. 
# program that asks a user to enter a positive number and then prints the hexadecimal
# equivalent of the number.

def hexa_equiv(number):
    """ A function that accepts a number from 0 to 15 and retuns its hexa value"""
    if number <= 9:
        return number
    else:
        if number == 10:
            return "A"
        elif number == 11:
            return "B"
        elif number == 12:
            return "C"
        elif number == 13:
            return "D"
        elif number == 14:
            return "E"
        else:
            return "F"
        
def reverse_string(str_to_rev):
    """A function that takes a string as parameter and reverses the string"""
    n = len(str_to_rev)
    rev_str = ""
    for i in range(n-1, -1, -1):
        rev_str+=  str_to_rev[i]
    return rev_str
        
def main(): 
    num = int(input("Enter a positive number: "))
    rem_str = ""
    number = num
    while number >0:
        rem = hexa_equiv(number % 16)
        number = number//16
        # join the remainder as string
        rem_str+=str(rem) 

    # reverse rem_str
    ret_str = reverse_string(rem_str)

    print("The binary equivalent of",num, "is",ret_str)

# Call the main function
main()
