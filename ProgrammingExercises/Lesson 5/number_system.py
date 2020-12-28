# A module called number_system that contains at least three functions:
# decimal_to_binary, decimal_to_octal and decimal_to_hexa that takes an integer
# parameter and respectively returns the parameter’s binary, octal and hexadecimal
# equivalent. You can create helper functions that can be called in the specified
# functions. Your module should have the capability to run as a standalone program
# and as a program that can be imported into another program. As a stand-alone program,
# your module should take a number as input and the base of conversion (2, 8, or 16).
# If the base of 2 is entered, your number should be converted to binary, if the base of
# 8 is entered, your number should be converted to octal, the base of 16 should convert
# your number to hexadecimal. Use input validation to ensure that the base is 2, 8 or 16.

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

def decimal_to_binary(num):
    rem_str = ""
    number = num
    while number > 0:
        rem = number % 2
        number = number//2
        # join the remainder as string
        rem_str+=str(rem) 

    # reverse rem_str
    ret_str = reverse_string(rem_str)
    return ret_str

def decimal_to_octal(num):
    rem_str = ""
    number = num
    while number > 0:
        rem = number % 8
        number = number//8
        # join the remainder as string
        rem_str+=str(rem) 

    # reverse rem_str
    ret_str = reverse_string(rem_str)
    return ret_str

def decimal_to_hexa(num):
    rem_str = ""
    number = num
    while number >0:
        rem = hexa_equiv(number % 16)
        number = number//16
        # join the remainder as string
        rem_str+=str(rem) 

    # reverse rem_str
    ret_str = reverse_string(rem_str)
    return ret_str

def main():
    # Get the number and conversion base as input
    num = int(input("Enter a number: "))
    base = int(input("Enter a base for conversion: "))
    # validate input for base
    while base != 2 and base != 8 and base != 16:
         base = int(input("Enter a base that is 2, 8 or 16: "))

    if base == 2:
        bin_str = decimal_to_binary(num)
        print(num,"converted to binary is", bin_str)
        
    if base == 8:
        oct_str = decimal_to_octal(num)
        print(num,"converted to octal is", oct_str)
    if base == 16:
        hex_str = decimal_to_hexa(num)
        print(num,"converted to hexadecimal is", hex_str)
        

# Call the main function conditionally
if __name__ == '__main__':
    main()
        
    
    

    
