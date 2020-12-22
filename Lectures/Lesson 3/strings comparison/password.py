# A program that checks password correctness
# using string comparison given that the correct
# password is secretcode

# Get password as input
password = input('Enter the password: ')
# Check that the password is correct
if password == "secretcode":
    print("Password accepted")
else:
    print("Wrong password, please try again!")
