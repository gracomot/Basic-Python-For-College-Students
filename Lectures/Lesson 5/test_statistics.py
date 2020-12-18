# A program that uses the statistics module to find
# the max, min, sum and average of some scores
import statistics
def main():
    # Get scores from the user
    list = statistics.get_input()
    min = statistics.find_minimum(list)
    max = statistics.find_maximum(list)
    sum = statistics.find_sum(list)
    avg = statistics.find_average(list)
    # Print the statistics
    statistics.displayStatistics(min, max, sum, avg)

# Call the main function
main()
    
    
