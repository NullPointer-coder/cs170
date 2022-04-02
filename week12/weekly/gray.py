# Jingbo Wang
# gray gifs

from graphics import *
def openImage(picFile):
    
    # loading it at 0,0
    img = Image(Point (0,0), picFile)
    width = img.getWidth() #row
    height = img.getHeight() # column
    img.move (width//2, height//2)
    win = GraphWin (picFile, width, height)
    img. draw (win)
    return img

def convertToGray(img):
    # nested 100p
    for row in range (img.getWidth()):
        for col in range (img.getHeight ()) :
            # these nested loops take us through each pixel,
            # as row, column
            r, g, b = img.getPixel(row,col) # gets you the pixel rgb
            i = round (0.299*r + 0.587*g + 0.114*b)
            img.setPixel(row,col, color_rgb(i, i, i)) # color rgb(r, g, b)
        update ()


#control function
def main():
    print ("This program converts an image to grayscale.")
    
    inFile = input ("Enter the name of a GIF file to convert: ")
    image = openImage(inFile)
    
    print ("Converting...", end="")
    convertToGray(image)
    print ("Done.")
    outFile = input("Enter filename for the converted image: ")
    image.save (outFile)
    
main()
