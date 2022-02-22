# Jingbo Wang
# a program that allows the user to draw a simple house
# using five mouse clicks and tree using eight mouse clicks.

from graphics import *

def house_five_point():
    win = GraphWin("Design a House",550, 550)
    win.setCoords(0, 0, 10.0, 10.0)

    message = Text(Point(5, 0.5), "Click on five points to design a house")
    message.draw(win)

    # Get and draw house frame
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Get house width
    house_width = abs(p2.getX() - p1.getX())

    # Use Polygon object to draw the house frame
    house = Rectangle(p1, p2)
    # rectangular.setOutline("black")
    house.draw(win)

    # Get and draw door
    p3 = win.getMouse()

    # Where is the bottom of the house frame
    if p1.getY() < p2.getY():
        p6Y = p1.getY()
    else:
        p6Y = p2.getY()

    # Get the door's width
    door_width = (1 / 5) * house_width

    p6 = Point(p3.getX() + (1 / 2) * door_width , p6Y)
    p7 = Point(p3.getX() - (1 / 2) * door_width , p3.getY())

    # Use Polygon object to draw the door
    door = Rectangle(p6, p7)
    door.setFill("red")
    door.draw(win)

    # Get and draw window
    p4 = win.getMouse()

    # Get the window's width
    window_width = (1 / 2) * door_width

    p8 = Point(p4.getX() - (1 / 2) * window_width
               , p4.getY() - (1 / 2) * window_width)
    p9 = Point(p4.getX() + (1 / 2) * window_width
               , p4.getY() + (1 / 2) * window_width)

    # Use Polygon object to draw the door
    window = Rectangle(p8, p9)
    window.draw(win)

    # Get and draw roof
    p5 = win.getMouse()

    # Get the Y of house top
    if p1.getY() < p2.getY():
        house_high = p2.getY()
    else:
        house_high = p1.getY()

    # Get left X of house
    if p1.getX() < p2.getX():
        p10X = p1.getX()
    else:
        p10X = p2.getX()


    p10 = Point(p10X, house_high)
    p11 = Point(p10X + house_width, house_high)

    # Use Polygon object to draw the roof
    roof = Polygon(p5, p10, p11)
    roof.setFill("black")
    roof.draw(win)


    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

def more_one_tree():
    win = GraphWin("Design a House",550, 550)
    win.setCoords(0, 0, 10.0, 10.0)

    message = Text(Point(5, 0.5), "Click on five points to design a house\n"
                   +" three more point to draw a tree")
    message.draw(win)

    # Get and draw house frame
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Get house width
    house_width = abs(p2.getX() - p1.getX())

    # Use Polygon object to draw the house frame
    house = Rectangle(p1, p2)
    # rectangular.setOutline("black")
    house.draw(win)

    # Get and draw door
    p3 = win.getMouse()

    # Where is the bottom of the house frame
    if p1.getY() < p2.getY():
        p6Y = p1.getY()
    else:
        p6Y = p2.getY()

    # Get the door's width
    door_width = (1 / 5) * house_width

    p6 = Point(p3.getX() + (1 / 2) * door_width , p6Y)
    p7 = Point(p3.getX() - (1 / 2) * door_width , p3.getY())

    # Use Polygon object to draw the door
    door = Rectangle(p6, p7)
    door.setFill("red")
    door.draw(win)

    # Get and draw window
    p4 = win.getMouse()

    # Get the window's width
    window_width = (1 / 2) * door_width

    p8 = Point(p4.getX() - (1 / 2) * window_width
               , p4.getY() - (1 / 2) * window_width)
    p9 = Point(p4.getX() + (1 / 2) * window_width
               , p4.getY() + (1 / 2) * window_width)

    # Use Polygon object to draw the door
    window = Rectangle(p8, p9)
    window.draw(win)

    # Get and draw roof
    p5 = win.getMouse()

    # Get the Y of house top
    if p1.getY() < p2.getY():
        house_high = p2.getY()
    else:
        house_high = p1.getY()

    # Get left X of house
    if p1.getX() < p2.getX():
        p10X = p1.getX()
    else:
        p10X = p2.getX()


    p10 = Point(p10X, house_high)
    p11 = Point(p10X + house_width, house_high)

    # Use Polygon object to draw the roof
    roof = Polygon(p5, p10, p11)
    roof.setFill("black")
    roof.draw(win)

    # Get and draw tree stump
    p12 = win.getMouse()
    p13 = win.getMouse()

    # Use Polygon object to draw the tree stump
    tree_stump = Rectangle(p12, p13)
    tree_stump.setFill("brown")
    tree_stump.draw(win)

    # Get and draw tree stump
    p14 = win.getMouse()

    # Use Polygon object to draw the leef
    tree_leef = Circle(p14, house_width / 2)
    tree_leef.setFill("green")
    tree_leef.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

    
def main():
    house_five_point()
    more_one_tree()


main()
