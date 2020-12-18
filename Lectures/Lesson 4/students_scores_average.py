# A program to that computes the average scores from a number of students
# Get input
students = int(input("Enter the number of students: "))
scores = int(input("Enter the number of scores for each student: "))

# Loop through each student  - Outer loop
for i in range(1, students+1):
    print("Student ",i," scores");
    print("-------------------")
    # Loop through each score - Inner loop
    total = 0 # initialize total to 0 for student
    for j in range(1, scores+1):
        score = int(input("Score "+str(j)+": "))
        total+=score
    avg = total/scores
    print("Student ",i," average: ",format(avg,'.2f'));
    print()
