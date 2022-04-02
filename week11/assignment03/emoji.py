# Jingbo Wang
# a program to draw a emoji
from graphics import *
import math

def drawFace(center, size, win):
    # face
    face = Circle(center, size)
    face.setFill('yellow')
    face.draw(win)

    
    centerX = center.getX()
    centerY = center.getY()

    eye_distance = 5 * math.sqrt(5) * size / 30
    eyeY = math.sqrt((eye_distance)**2 / 5)
    eyeX = 2 * eyeY
    eyesize =  8 * size / 30
    eyeballsize = 4 * size / 30

    # eye
    eye1 = Circle(Point(centerX - eyeX, centerY + eyeY), eyesize)
    eye1.setFill('white')
    eye1.draw(win)

    eyeball1 = Circle(Point(centerX - eyeX, centerY + eyeY + (eyesize / 2))
                      , eyeballsize)
    eyeball1.setFill('black')
    eyeball1.draw(win)

    eye2 = Circle(Point(centerX + eyeX, centerY + eyeY), eyesize)
    eye2.setFill('white')
    eye2.draw(win)

    eyeball2 = Circle(Point(centerX + eyeX, centerY + eyeY + (eyesize / 2))
                      , eyeballsize)
    eyeball2.setFill('black')
    eyeball2.draw(win)

    mouth_right_distance = 5 * math.sqrt(13) * size / 30
    mouth_right_Y = (mouth_right_distance * 15) / (5 * math.sqrt(13)) 
    mouthY_center = ((centerY - mouth_right_Y)
                     + (centerY - mouth_right_Y - eyesize / 8)) / 2

    # mouth
    mouth = Rectangle(Point(centerX - eyeX,
                            centerY - mouth_right_Y - eyesize / 8),
                      Point(centerX + eyeX, centerY - mouth_right_Y))
    mouth.setOutline('red')
    mouth.setFill('red')
    mouth.draw(win)
    mouth1 = Circle(Point(centerX - eyeX, mouthY_center), 0.5 * size / 30)
    mouth1.setOutline('red')
    mouth1.setFill('red')
    mouth1.draw(win)
    mouth2 = Circle(Point(centerX + eyeX, mouthY_center), 0.5 * size / 30)
    mouth2.setOutline('red')
    mouth2.setFill('red')
    mouth2.draw(win)

def drawFace2(center, size, color, win):
    # face
    face = Circle(center, size)
    face.setFill(color)
    face.draw(win)

    
    centerX = center.getX()
    centerY = center.getY()

    eye_distance = 5 * math.sqrt(5) * size / 30
    eyeY = math.sqrt((eye_distance)**2 / 5)
    eyeX = 2 * eyeY
    eyesize =  8 * size / 30
    eyeballsize = 4 * size / 30

    # eye
    eye1 = Circle(Point(centerX - eyeX, centerY + eyeY), eyesize)
    eye1.setFill('white')
    eye1.draw(win)

    eyeball1 = Circle(Point(centerX - eyeX, centerY + eyeY + (eyesize / 2))
                      , eyeballsize)
    eyeball1.setFill('black')
    eyeball1.draw(win)

    eye2 = Circle(Point(centerX + eyeX, centerY + eyeY), eyesize)
    eye2.setFill('white')
    eye2.draw(win)

    eyeball2 = Circle(Point(centerX + eyeX, centerY + eyeY + (eyesize / 2))
                      , eyeballsize)
    eyeball2.setFill('black')
    eyeball2.draw(win)

    mouth_right_distance = 5 * math.sqrt(13) * size / 30
    mouth_right_Y = (mouth_right_distance * 15) / (5 * math.sqrt(13)) 
    mouthY_center = ((centerY - mouth_right_Y)
                     + (centerY - mouth_right_Y - eyesize / 8)) / 2

    # mouth
    mouth = Rectangle(Point(centerX - eyeX,
                            centerY - mouth_right_Y - eyesize / 8),
                      Point(centerX + eyeX, centerY - mouth_right_Y))
    mouth.setOutline('red')
    mouth.setFill('red')
    mouth.draw(win)
    mouth1 = Circle(Point(centerX - eyeX, mouthY_center), 0.5 * size / 30)
    mouth1.setOutline('red')
    mouth1.setFill('red')
    mouth1.draw(win)
    mouth2 = Circle(Point(centerX + eyeX, mouthY_center), 0.5 * size / 30)
    mouth2.setOutline('red')
    mouth2.setFill('red')
    mouth2.draw(win)
    
def main():
    # set up for window
    win = GraphWin("Emoji",600, 600)
    win.setCoords(0, 0, 100.0, 100.0)

    # ask user for center point and size
    center = input("Input a center point(Like: 10 20): ")
    center = center.split()
    center = Point(float(center[0]), float(center[1]))
    size = int(input("Input a face size: "))

    # call function
    drawFace(center, size, win)

    done = "y"
    while (done == "y"):
       print()
       print("Draw another face!")
       center = input("Input a center point(Like: 10 20): ")
       center = center.split()
       center = Point(float(center[0]), float(center[1]))
       size = int(input("Input a face size: "))
       color = input("Input a color of face: ")
       drawFace2(center, size, color, win)

       # ask to exit or not
       done = input("Continue drawing a face (y: Yes / n: No): ")
    print("Finished drow face!")
main()
