# A program that simulates the rolling of a die
import random

def main():
    my_guess = int(input("Enter your guess from 1 to 6: "))
    the_number = random.randint(1,6)
    if (my_guess == the_number):
        print("You guessed right")
    else:
        print("Your guess is wrong. The chosen number is",the_number)

# Call the main function
main()
