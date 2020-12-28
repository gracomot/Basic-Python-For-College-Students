# A program that demonstrates the use of keyword arguments
# It reverses a person's name

def reverse_name(firstname, lastname):
    print("Your name reversed is",lastname, firstname)

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    reverse_name(lastname = last_name, firstname = first_name)

# Call the main function
main()
