# A program that prints a person's personal info

def print_info(name, age, address):
    print("My name is ",name,", I am ",age,
          " years old. My address is ",address,sep='')
    print("In 5 years time,","I will be",(age+5),"years old.")

def main():
    # Get input from the user
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    print_info(name, age, address)

# Call the main function
main()
