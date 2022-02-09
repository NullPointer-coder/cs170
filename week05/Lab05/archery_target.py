# Jingbo Wang
# imports graphics lib
# the program is to print a archery target

from graphics import *

# math.
# object of GraphWin class, init title width, height
win = GraphWin('Archery Target', 500, 500)


# Circle
# object Point, x coord, y coord, calling constr
center = Point(250, 250)

# white cricle
white_cricle = Circle(center, 200)
white_cricle.setFill('white')
white_cricle.draw(win)

# black cricle
black_cricle = Circle(center, 160)
black_cricle.setFill('black')
black_cricle.draw(win)

# blue crile
blue_crile = Circle(center, 120)
blue_crile.setFill('blue')
blue_crile.draw(win)

# red cricle
red_cricle = Circle(center, 80)
red_cricle.setFill('red')
red_cricle.draw(win)

# yellow cricle
yellow_cricle = Circle(center, 40)
yellow_cricle.setFill('yellow')
yellow_cricle.draw(win)
