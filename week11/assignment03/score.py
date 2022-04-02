# Jingbo Wang
#to print out the score of each student from score.txt

from tkinter.filedialog import askopenfilename
from graphics import *

def main():
    # build for window
    win = GraphWin("Student Score", 600, 600)
    win.setCoords(0, 0, 100.0, 100.0)

    Y1 = 92.5
    Y2 = 95
    Y3 = 90
    
    # open the file by GUI
    in_file_Name = askopenfilename()
    in_file = open(in_file_Name, "r")
    
    for line in in_file:
        line = line.split()
        # get students' name
        name = ""
        for j in range(len(line)):
            if(not(line[j].isnumeric())):
                name = line[j] + " " + name
        name = name.strip(" ")
        
        # draw student name
        student_name = Text(Point(10, Y1), name)
        student_name.draw(win)
        Y1 -= 10
        
        # get students' score
        score = int(line[len(line) - 1])
        p1 = Point(20, Y2)
        p2 = Point((score/100*60) + 20, Y3)
        student_score = Rectangle(p1, p2)
        # draw the rectangle for each student's score
        student_score.draw(win)
        Y2 -= 10
        Y3 -= 10
    in_file.close() 
main()
