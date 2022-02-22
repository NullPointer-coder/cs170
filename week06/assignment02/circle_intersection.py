# Jingbo Wang
# a program that computes the intersection of a circle
# with a horizontal line and displays the information
# textually and graphically

from cmath import sqrt
from graphics import *
import math
def main():
  print("This program computes the intersection of a circle and")
  print("a horizontal line.")
  print()
  radius = float(input("Please enter the radius of the circle: "))
  y_inter = float(input("Please enter the y-intercept of the line: "))
  win = GraphWin("Circle Intersection",500,500)
  win.setCoords(-10,-10,10,10)

  center = Point (0, 0)
  # draw the circle
  circle = Circle(center, radius)
  circle.setFill("green")
  circle.draw(win)

  #draw the Cartesion coordinate system
  Xline = Line(Point(-10, 0), Point(10, 0))
  Xline.draw(win)
  Yline = Line(Point(0, -10), Point(0, 10))
  Yline.draw(win)
  msg3 = Text(Point(-0.5, - 0.5), "(0,0)")
  msg3.draw(win)
  msg4 = Text(Point(9.5, 0.5), "x")
  msg4.draw(win)
  msg5 = Text(Point(0.5, 9.5), "y")
  msg5.draw(win)

 # draw the line
  line = Line(Point(-10, y_inter), Point(10, y_inter))
  line.draw(win)
  
  msg0 = Text(Point(-0.7, y_inter - 0.5), "y = " + str(y_inter))
  msg0.draw(win)
  
  x1 = abs(sqrt(radius**2 - y_inter**2 ))
  x2 = -abs(sqrt(radius**2 - y_inter**2 ))
  p1 = Point(x1, y_inter)
  p1.draw(win)
  p1.setOutline("red")

  p2 =Point(x2, y_inter)
  p2.draw(win)
  p2.setOutline("red")

  msg1 = Text(Point(x1, y_inter + 1), x1)
  msg1.draw(win)
  
  msg2 = Text(Point(x2, y_inter + 1), x2)
  msg2.draw(win)

main()
