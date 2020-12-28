# A program to show how local scoping works
x = 100 # A global variable that is  accessible to all statements

def myfunc():
    print("Function myfunc can access the global variable x")
    print("Variable x is ",x)

def main():
    myfunc()
    # main function tries to access variable x
    print("Main function can access the global variable x")
    print("Variable x is ",x)

main()
