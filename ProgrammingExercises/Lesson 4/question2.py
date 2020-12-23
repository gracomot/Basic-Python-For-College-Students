# Question 2 (Multiplication Table)
# Modify the multiplication table program discussed in this lesson
# such that your program takes the number of rows and the number of
# colums as input. It them displays the multiplication table corresponding
# to the entered rows and columns.

# Get the number of rows and columns from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
           
# Print the header
for i in range(1,cols+1):
     print("------",end="")
print() 
for i in range(1,cols+1):
    if i == 1:
        print(format(i,'8d'),end = " ")
    else:
        print(format(i,'4d'),end = " ")
print()
for i in range(1,cols+1):
     print("------",end="")
print()

# The outer loop representing the rows of the multiplication table
for i in range(1,rows+1):
    print(format(i,'2d'),end = "|")
# The inner loop representing the columns of the multiplication table
    for j in range(1,cols+1):
        print(format(i*j, '5d'), end = "")
    print()

