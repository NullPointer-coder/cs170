# Jingbo Wang
#to print out the score of each student from score.txt

from tkinter.filedialog import askopenfilename
from graphics import *

def main():
    # build for window
    win = GraphWin("Student Score", 700, 700)
    win.setCoords(0, 0, 100.0, 100.0)
    
    # open the file by GUI
    file_name = askopenfilename()
    infile = open(file_name, "r")

    
    nameY = 82.5
    socre_left_Y = 85
    score_right_Y = 80
    
    for line in infile:
        line = line.split()
        
        # get students' name
        name = line[0]
        # draw student name
        student_name = Text(Point(20, nameY), name)
        student_name.draw(win)
        nameY -= 8
        
        # get students' score
        score = int(line[1])
        p1 = Point(30, socre_left_Y)
        p2 = Point((score / 100 * 50) + 30, score_right_Y)
        student_score = Rectangle(p1, p2)
        # draw the rectangle for each student's score
        student_score.draw(win)
        socre_left_Y -= 8
        score_right_Y -= 8
    infile.close()
main()
