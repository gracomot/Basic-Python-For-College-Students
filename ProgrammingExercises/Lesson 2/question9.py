# Some cookies are to be shared among three people
# Write a program that will ask for the number of cookies
# and the percentages to be given to the first, second
# and third person and then displays the number of cookies each person gets.

# Get the number of cookies to be shared
cookies = int(input("Enter the number of cookies to be shared: "))
# Get the percentages of the cookies each person will get
pct1 = float(input("Enter the percentage (%) of the total cookies the first person will get: "))
pct2 = float(input("Enter the percentage (%) of the total cookies the second person will get: "))
pct3 = float(input("Enter the percentage (%) of the total cookies the third person will get: "))

# Calculate the number of cookies each perso will get
cookies_num1 = (pct1/100) * cookies
cookies_num2 = (pct2/100) * cookies
cookies_num3 = (pct3/100) * cookies

# print the number of cookies each person gets
print("First person: ",format(cookies_num1,'.2f'),"cookies")
print("Second person: ",format(cookies_num2,'.2f'),"cookies")
print("Third person: ",format(cookies_num3,'.2f'),"cookies")
