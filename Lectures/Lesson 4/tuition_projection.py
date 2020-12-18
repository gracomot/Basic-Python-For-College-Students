# A program to project the tuition for a specified  number of years
# given a 5% tuition increase every year

# Get input from the use

tuition = float(input("Enter the current tuition: "))
year =  int(input("Enter the number of years for tuition increase: "))

count = 1

# print the heading
print('Year','\t','Projected Tuition')

while count <= year:
    increase = (tuition*0.05)
    tuition = tuition + increase # tuition+=increase
    print(count,'\t', format((tuition),',.2f'))
    # count=count+1
print("Thank you")
