# A program that ask for temperature in fahrenheit and
# converts it to celsuis. The formular for converting
# fahrenheit to celsius is (F − 32) × 5/9

# Ask for the temperature in fahrenheit
temp_in_fah = float(input('Enter temperature in Fahrenheit: '))
# Convert temperature to celsius
temp_in_cels = (temp_in_fah - 32)* (5/9)
# Display temperature in celsius
print(temp_in_fah,"degree fahrenheit is equivalent to",format(temp_in_cels,'.2f'),"degree celsius")

