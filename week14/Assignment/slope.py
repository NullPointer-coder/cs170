# Jingbo Wang
# slope.py
# a program to calculate the slope and length of the line

from graphics import *
import math

def main():
    win = GraphWin("Slope and Length",550, 550)
    win.setCoords(0, 0, 10.0, 10.0)

    #set the Text control
    message = Text(Point(5, 0.5), " ")
    message.draw(win)

    # Get the line
    p1 = win.getMouse()
    p2 = win.getMouse()

    try:        
        # calc the slope and length of line
        slope = (p1.getY() - p2.getY()) / (p1.getX() - p2.getX())
        length = math.sqrt((p1.getY() - p2.getY())**2
                               + (p1.getX() - p2.getX())**2)
        # Get and draw mind point 
        mid_point = Point(abs(p1.getX() + p2.getX()) / 2,
                          abs(p1.getY() + p2.getY()) / 2)
        mid_point.setOutline("red")
        mid_point.draw(win)
    
         # draw the line
        line = Line(p1,p2)
        line.draw(win)
        
        #set the final resalt  
        message.setText("slope: "+ str(slope) + "\n length: "+ str(length)) 
    except ZeroDivisionError:
        # if divide by zero
        print("Can not divide by zero; don't click at same place!")
        win.close()
main()
