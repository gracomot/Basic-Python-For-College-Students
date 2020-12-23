# Question 1 (Tuition Projection)
# It was announced at a University that the tuition for a full-time student
# will increase by 5% each year going forward. Write a program that allows
# users to enter the current tuition. Your program should display when the tuition
# will be equal or greater the double of the initial tuition.
# Your output should look like the one shown below;
#		In n years, the tuition would have doubled the initial tuition
# Note: The tuition does not have to exactly double the initial tuition.

tuition = float(input("Enter the current tuition: "))
DOUBLE_TUITION = tuition*2
count = 0

# print the heading
print('Year','\t','Projected Tuition')

while tuition < DOUBLE_TUITION:
    count=count+1
    increase = (tuition*0.05)
    tuition = tuition + increase # tuition+=increase
    print(count,'\t', format((tuition),',.2f'))
    
print("In ", count,"years,", "the tuition would have doubled")
