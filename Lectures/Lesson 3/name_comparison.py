# A program that takes two names
# and deterines which is greater

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Compare the names
if name1 > name2:
    print(name1,'is greater than', name2)
elif name2 > name1:
    print(name2,'is greater than', name1)
else:
    print(name1,'is equal to',name2)
    
