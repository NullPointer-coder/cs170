# Jingbo Wang
# Program to copy a file's content to new file imitating
# copy-paste operation using tkinter

import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def main():
    # get the file name
    in_file_Name = askopenfilename() # gives the absolute path of selected file, or ""
    out_file_Name = asksaveasfilename() # gives the absolute path of selected file, or ""

    # open the files
    in_file = open(in_file_Name, "r")
    out_file = open(out_file_Name, "w")

    # process each line of the input file
    for line in in_file.readline():
        print(line.strip(), file=out_file)

    #close both files
    in_file.close()
    out_file.close()
    print("+++File copied+++")
main()
