# Question 8 (Average Age)
# Write a program that asks users for the ages of students in a class
# until a sentinel is entered. Your program should print the average
# age of the students in the class.

# Get the age of the first student
age = int(input("Enter the a student's age: "))
total = 0
count = 0
while age != -1:
    total+=age
    count+=1
    age = int(input("Enter the a student's age: "))
avg = total/count
print("The average age of the students in the class is",avg)

    
