# Jingbo Wang
# Program to copy a file's content to new file imitating
# copy-paste operation using tkinter

import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def main():
    # gives the absolute path of selected file, or ""
    in_file_Name = askopenfilename() 

    # open the files
    in_file = open(in_file_Name, "r")

    lines = 0
    word_sum = 0
    char_sum = 0
    
    # process each line of the input file
    for line in in_file:
       if(len(line) > 1):
           lines += 1
           line.strip()
           words = line.split()
           word_sum += len(words)
           for i in range(len(words)):
               word = words[i]
               for j in range(len(word)):
                   if(word[j].isalpha()):
                       char_sum += 1

    #close both files
    in_file.close()

    #print reasult
    print("Total lines:",lines)
    print("Total words:",word_sum)
    print("Total characters:",char_sum)
    
main() 
