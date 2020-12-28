# Write a program that takes a number as input and the base of conversion (2, 8, or 16).
# If the base of 2 is entered, your number should be converted to binary, if the base of
# 8 is entered, your number should be converted to octal, the base of 16 should convert
# your number to hexadecimal. The conversion should be done by using the functions from
# the number_system module in question 7 . Use input validation to ensure that the base
# is 2, 8 or 16.

import number_system
def main():
    # Get the number and conversion base as input
    num = int(input("Enter a number: "))
    base = int(input("Enter a base for conversion: "))
    # validate input for base
    while base != 2 and base != 8 and base != 16:
         base = int(input("Enter a base that is 2, 8 or 16: "))

    if base == 2:
        bin_str = number_system.decimal_to_binary(num)
        print(num,"converted to binary is", bin_str)
        
    elif base == 8:
        oct_str = number_system.decimal_to_octal(num)
        print(num,"converted to octal is", oct_str)
    else:
        hex_str = number_system.decimal_to_hexa(num)
        print(num,"converted to hexadecimal is", hex_str)

#   Call the main function
main()

    
