# student_score.py
# Program to show students' score by bars
# by Fengfan Zhang

from tkinter.filedialog import askopenfilename
from graphics import *

def student_score():
    # Ask open the file
    in_file_name = askopenfilename()
    in_file = open(in_file_name, "r")

    # Draw the canvas
    win = GraphWin("score_bars", 330, 330)
    win.setCoords(0, 0, 200, 200)
    # Show the number of students
    Text(Point(70, 180), "The number of students is:").draw(win)
    number = in_file.readline()[0]  # The first line which contains the count.
    Text(Point(130, 180), number).draw(win)
    
    y = 160
    for contents in in_file.readlines():
        # Draw the names.
        name = contents.split()[0]
        message = Text(Point(30, y), name)
        message.draw(win)
        # Draw the bars of score.
        score = contents.split()[1]
        message = Text(Point(180, y), score)
        message.draw(win)
        p1 = Point(60, y+5)
        p2 = Point(60 + int(score), y-5)
        Rectangle(p1, p2).draw(win)
        y -= 20
    # Close the file
    in_file.close()


student_score()
