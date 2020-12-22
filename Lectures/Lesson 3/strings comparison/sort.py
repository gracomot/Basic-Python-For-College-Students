# A program that sorts two names in alphabetical order
# by using string comparison

# Accept the input of the two names
name1 = input('Please enter a name: ')
name2 = input('Please enter another name: ')

# Compare the two names
print("The names sorted in alphabetic order are: ")
if (name1 < name2):
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
