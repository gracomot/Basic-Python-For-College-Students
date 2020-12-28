# A program to demonstrate that changes to
# parameters do not affect argument values

def arg_func(myargument):
    print("Function arg_func will be doubling the value of myargument")
    myargument = myargument*2
    print("The new value of myargument is",myargument)

def main():
    arg_value = 20
    print("The value of arg_value before calling the arg_func function is",arg_value)
    print("arg_value is passed to the arg_func parameter")
    # call the arg_func function
    arg_func(arg_value)
    print("The value of arg_value after calling the arg_func function is", arg_value)

# Call the main method
main()
