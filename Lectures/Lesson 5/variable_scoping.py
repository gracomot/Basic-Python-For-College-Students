# A program to show how local scoping works
def myfunc():
    x = 100 # A local variable only accessible to myfunc function
    print("Function myfunc can access variable x")
    print("Variable x is ",x)

def main():
    myfunc()
    # main function tries to access variable x
    print("Main function tries to access the local variable in myfunc")
    print("Variable x is ",x)

main()
