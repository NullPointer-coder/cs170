# Jingbo Wang
# imports graphics lib
# this lib has a lot of readymade stuff
# readymade stuff could be functions
# or readymade stuff could be classes
# import graphics
# this line means import 'everything' from graphics
from graphics import *

# creates a graphics window for you, parent window
# if you want to use anything from graphics library, prefixit with graphics.
# <library>.
# math.
# object of GraphWin class, init title width, height
win = GraphWin('shapes', 400, 400)


# Point
a_point = Point(10, 100)
# this line uses object!!
# you can use object to access class stuff
a_point.draw(win)
# gets us the x & y coordinates
print(a_point.getX())
print(a_point.getY())


# Circle
# object Point, x coord, y coord, calling constr
center = Point(100, 100)
# this object circ represents a circle with center 100, 100 and radius 30
# creatiing Circle object, calling constructor, init Point (center), radius
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)

# label is just some text drawn on to the window, Text
# first argument is the point, second argument is the text
label = Text(center, "Red Circle")
label.draw(win)

# rectangle
rect_p1 = Point(30, 30)
rect_p2 = Point(100, 70)
rect = Rectangle(rect_p1, rect_p2)
rect.draw(win)

# line
line = Line(Point(20, 30), Point(180, 165))
line.draw(win)

# oval
oval = Oval(Point(20, 150), Point(180, 199))
oval.draw(win)
