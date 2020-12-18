# A program that uses a loop to takes n test scores
# from a student and finds the average score 

how_many = int(input("Enter number of test scores: "))
#Get all the scores from the student
total = 0.0
for i in range(1,how_many+1):# 1 ... how_many
    score = int(input("Enter score "+str(i)+": "))
    total += score  # total = total + score
avg = total/how_many
# Display the total score
print("Total score: ",format(total,'.2f'))
# Display the average score
print("Average score: ",format(avg,'.2f'))

