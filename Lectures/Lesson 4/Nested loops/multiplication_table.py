# A Program to display the multiplication table from 1 to 12

# Print the header
for i in range(1,13):
     print("------",end="")
print() 
for i in range(1,13):
    if i == 1:
        print(format(i,'8d'),end = " ")
    else:
        print(format(i,'4d'),end = " ")
print()
for i in range(1,13):
     print("------",end="")
print()

# The outer loop representing the rows of the multiplication table
for i in range(1,13):
    print(format(i,'2d'),end = "|")
# The inner loop representing the columns of the multiplication table
    for j in range(1,13):
        print(format(i*j, '5d'), end = "")
    print()

