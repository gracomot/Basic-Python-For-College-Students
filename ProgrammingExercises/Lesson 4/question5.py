# Question 5 (Special Diet for weight loss)
# Your friend told you about a special diet for losing weight that you seem interested about.
# The special diet allows you to consistently lose some weight every month.
# Write a program that allows you to enter you current weight(in pounds) and the weight (in pounds)
# that will be lost every month. Your program should display what your new weight will be at the
# end of every month until you have lost at most half of your weight.
# Your program should also display a message that says
# "In n months of joining the weight loss program, you would have lost half of your weight.",
# where n is the months it takes to be at most half the size of your weight

# Get the initial weight as input
weight = int(input("Enter your current weight: "))
pound_lost = int(input("Enter the pounds you will lose every month: "))
count = 0

# print the heading
print('Weight','\t','Projected Weight')

DOUBLE_WEIGHT = weight*0.5
while weight > DOUBLE_WEIGHT:
    count += 1
    weight-=pound_lost
    print(count,'\t', weight)

# Print summary
print("In", count,"months of joining the weight loss program you would have lost half of your current weight")

    
