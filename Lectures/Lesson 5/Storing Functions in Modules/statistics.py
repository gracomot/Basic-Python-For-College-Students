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
            min = list_of_scores[i]
    return min

# A function that find the maximum of a list of scores
def find_maximum(list_of_scores):
    score_count = len(list_of_scores)
    max =  0
    for i in range(score_count):
        if list_of_scores[i] > max:
            max = list_of_scores[i]
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
def displayStatistics(min, max, total, avg):
    print("The minimum score is",min)
    print("The maximum score is",max)
    print("The total score is",  total)
    print("The average score is",format(avg,".2f"))
# The main function
def main():
    list_of_scores = get_input()
    min =  find_minimum(list_of_scores)
    max = find_maximum(list_of_scores)
    total = find_sum(list_of_scores)
    avg = find_average(list_of_scores)
    displayStatistics(min, max, total, avg)

# Call the main function
if __name__ == '__main__':
    main()
    
