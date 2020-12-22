# A program to determine the letter grades of students
# based on their test scores

# Get the score as input
score = int(input('Enter your score: '))
# Determine the letter grade
if (score >= 0 and score <=100):
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
else:
    print("Your score is invalid")
