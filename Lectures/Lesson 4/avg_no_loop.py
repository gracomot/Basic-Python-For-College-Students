# A program that takes 10 test scores from a
# student and finds the average score

#Get all the scores from the student
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
score4 = int(input("Enter score 4: "))
score5 = int(input("Enter score 5: "))
score6 = int(input("Enter score 6: "))
score7 = int(input("Enter score 7: "))
score8 = int(input("Enter score 8: "))
score9 = int(input("Enter score 9: "))
score10 = int(input("Enter score 10: "))

# Find the average score
avg = (score1+score2+score3+score4+score5+score6+score7+score8+score9+score10)/10
# Display the average score
print("Average score: ",format(avg,'.2f'))

