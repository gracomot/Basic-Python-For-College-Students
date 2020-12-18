# A program to compute the simple interest on a loan
def simple_interest(principal, rate, time):
    return (principal*rate*time)
def main():
    interest = simple_interest(5000, 0.06, time = 2)
    print("The simple interest is $",interest,sep='')

# Call the main function
main()
