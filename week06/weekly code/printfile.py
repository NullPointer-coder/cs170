# Jingbo Wang
# Prints a file to the screen.

def main():
  # asking user for giving the input file name
  fname = input("Enter filename: ")
  # open the file object, associates a file object with an actual file
  infile = open(fname,"r")
  # read the content of the file
  data = infile.read()
  print(data)

main()
