# Jingbo Wang
# This program is to calculate the number of words in this sentence
# and the average word length of it.

import math
def main():
    print("This program is to calculate the number "
          + "of words in this sentence\n and the average "
          + "word length of it.")
    
    # Get a string
    string = input("Please enter a sentence: ")

    string = string.split()

    number_of_words = 0
    words_length = 0

    # get number of words in this sentence
    for word in string:
        number_of_words += 1
        
        # get the total length of words
        words_length += len(word)

    # calculate the average word length   
    average_words_length = math.floor(words_length / number_of_words)
    
    print("Number of words = " + str(number_of_words))
    print("Average word length = " + str(average_words_length)
          + " letters")

main()
