# A program that uses a sentinel controlled while loop to take
# repeatedly take test scores from a student and finds the average score 

# Declare variables
total = 0.0
count = 0
score = float(input("Enter score "+str(count+1)+": "))
#Get all the scores from the student
while(score != -1):
    count=count+1
    total = total + score
    score = float(input("Enter score "+str(count+1)+": "))

# Find the average score
if count > 0:
    avg = total/count
    # Display the sum and average score
    print("Total score: ",format(total,'.2f'))
    print("Average score: ",format(avg,'.2f'))
else:
    print("You have no valid scores to process")
