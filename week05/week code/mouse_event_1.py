# Jingbo Wang
# This program is to print where you click at

from graphics import *

# object of GraphWin class
win = GraphWin("Click Me!")

# get mouse action
p = win.getMouse()

# print where you click at
print("You clicked at: ", p.getX(), p.getY())
