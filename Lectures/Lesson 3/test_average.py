# program that allows a student to enter scores for three test
# and display the average score and a congratulatory message
# if average score is greater than 95

# input all three test scores
test1 = int(input("Enter the score for test 1: "))
test2 = int(input("Enter the score for test 2: "))
test3 = int(input("Enter the score for test 3: "))

# find the average of the three test scores
avg_score = (test1 + test2 + test3)/3

#print the average score
print("Average score: ", format(avg_score, '5.2f'))

# print a congratulatory message if average score is greater than 95
if avg_score > 95:
    print("Congratulations!\nYour performance is impressive!")
else:
    print('There is room for improvement')
print('Have a great holiday')
