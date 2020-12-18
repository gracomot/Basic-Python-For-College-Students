# A program that takes a list of scores and
# displays the minimum and maximum of those scores
def min_max(list):
    count = len(list)
    # initialize min and max
    min = 100
    max = 0
    for i in range(count):
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]
    return (min,max)

def get_scores():
    list = []
    # Get input from user
    score = int(input("Enter a score: "))
    while score != -1:
        list.append(score)
        score = int(input("Enter a score or -1 if there is no more score: "))
    return list

def main():
    list = get_scores()
    min,max = min_max(list)
    print("The min score is",min,"and the maximum score is",max)

# Call the main function
main()
        
        


        
        
