# A program to determine the letter grades of students
# based on their test scores

# Get the score as input
score = int(input('Enter your score: '))
# Validate the score entered
while score < 0 or score > 100:
    print("ERROR: Invalid Input, score must be betweeen 0 and 100")
    score = int(input('Enter a valid score: '))
# Determine the letter grade
if score >= 90:
    print('Letter grade: A')
elif score >= 80:
    print('Letter grade: B')
elif score >= 70:
    print('Letter grade: C')
elif score >= 60:
    print('Letter grade: D')
else:
    print('Letter grade: F')
