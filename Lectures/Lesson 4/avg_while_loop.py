# A program that uses while loop to takes n test scores
# from a student and finds the average score 

how_many = int(input("Enter number of test scores: "))
# Declare variables
total = 0.0
count = 0

#Get all the scores from the student
while(count < how_many):
    total = total + int(input("Enter score "+str(count+1)+": "))
    count=count+1 #count+=1
    
# Print the total score
print("Total score: ",format(total,'.2f'))
# Find the average score
avg = total/how_many
# Display the average score
print("Average score: ",format(avg,'.2f'))
