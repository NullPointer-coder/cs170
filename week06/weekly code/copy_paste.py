# Jingbo Wang
# Promgram to copy a file's content to
# a new file imitating copy-paste operaton.

def main():
    # get the file name
    infileName = input("Name of the file to copy: ")
    outfileName = input("Name of the new file: ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
      print(line, file=outfile)

    #close both files
    infile.close()
    outfile.close()
    print("+++File copied+++", outfileName)
main()
