# grade.py
# A program that output the student's score by bars
# Linna

from graphics import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def bar():
    # open the file
    input_file_name = askopenfilename()
    input_file = open(input_file_name, 'r')
    # input the graph
    win = GraphWin("Stundent grade", 300, 300)
    win.setBackground("white")
    # main function
    x = []
    y = []
    n = int(input_file.readline())
    for i in range(n):
        line = input_file.readline()
        line = line.split()
        x.append(line[0])
        y.append(int(line[1]))

    # input the students' name
    Text(Point(25, 180), x[3]).draw(win)
    Text(Point(25, 130), x[2]).draw(win)
    Text(Point(31, 80), x[1]).draw(win)
    Text(Point(35, 30), x[0]).draw(win)
    # draw the bars
    bar = Rectangle(Point(80, 30), Point(80 + y[0], 30))
    bar.setWidth(10)
    bar.draw(win)
    bar_2 = Rectangle(Point(80, 80), Point(80 + y[1], 80))
    bar_2.setWidth(10)
    bar_2.draw(win)
    bar_3 = Rectangle(Point(80, 130), Point(80 + y[2], 130))
    bar_3.setWidth(10)
    bar_3.draw(win)
    bar_4 = Rectangle(Point(80, 180), Point(80 + y[3], 180))
    bar_4.setWidth(10)
    bar_4.draw(win)


bar()
