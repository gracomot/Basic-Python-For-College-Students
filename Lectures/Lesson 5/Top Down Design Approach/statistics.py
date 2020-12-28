# program that takes a list of scores and displays the minimum,
# maximum, sum and average of the scores
def get_input():
    list_of_scores = []
    score = int(input("Enter a score: "))
    while(score != -1):
        list_of_scores.append(score)
        score = int(input("Enter a score or -1 if there is not more score: "))
    return list_of_scores
    
# A function that find the minimum of a list of scores
def find_minimum(list_of_scores):
    score_count = len(list_of_scores)
    min =  100
    for i in range(score_count):
        if list_of_scores[i] < min:
            min = score[i]
    return min

# A function that find the maximum of a list of scores
def find_maximum(list_of_scores):
    score_count = len(list_of_scores)
    max =  0
    for i in range(score_count):
        if list_of_scores[i] > min:
            max = score[i]
    return max

# A function that find the sum of a list of scores
def find_sum(list_of_scores):
    score_count = len(list_of_scores)
    total =  0
    for i in range(score_count):
        total+= list_of_scores[i]
    return total

# A function that finds the average of a list of scores
def find_average(list_of_scores):
    score_count = len(list_of_scores)
    total = find_sum(list_of_scores)
    avg = total/score_count
    return avg

# A function that displays the computed statistics
def displayStatistics(list_of_scores):
    print("The minimum score is",find_minimum(list_of_scores))
    print("The maximum score is",find_maximum(list_of_scores))
    print("The total score is",  find_sum(list_of_scores))
    print("The average score is",find_average(list_of_scores))
# The main function
def main():
    list_of_scores = get_input()
    displayStatistics(list_of_scores)

# Call the main function
main()
    
