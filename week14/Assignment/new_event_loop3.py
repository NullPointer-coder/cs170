# new_event_loop3.py -- color changing window
# Jingbo Wang
# A program to print each color on board and can type text on it
# new funtcion is discarding anything that user may have typed in the box

from graphics import *

def handleKey(k, win):
    if k == "r":
         win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")
        
def handleClick(pt, win):
    # create an Entery fot user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    # Go modal: wait until user types Return or Escape Key
    while True:
        key = win.getKey()
        if key == "Return":
            break
        if key == "Escape":
            entry.setText("") # "Escape" to empty
            break
    
    # undraw the entry and draw text
    entry.undraw()
    Text(pt, entry.getText()).draw(win)

def main():
    win = GraphWin("Click and Type", 500, 500)
    # Event Loop: handle key presses and mouse clicks until user
    # presses the "q" key.
    while True:
        key = win.checkKey()
        if key == "q": # loop exit
            break
        if key:
            handleKey(key, win)
            # call the handleKey function to change the background color
            # if user wants
        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)
    win.close()
    # close window

main()

