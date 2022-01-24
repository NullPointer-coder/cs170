# Jingbo Wang
# A simple program to average four scores
# Illustrates use of multiple input

def main():
    print("This program computs the average of four exam scores.")

    total_score = 0;

    # input 4 different value from user
    for i in range(4):
        score = eval(input("Please enter score: "))
        # add innput scores together 
        total_score += score
        
    # calculate the average score
    average_score = total_score/4
    
    # print the average score
    print("The average of the score is:", average_score)

main()
