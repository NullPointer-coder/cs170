# average6.py
# Jingbo Wang
#     Computes the average of numbers listed in a file.

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + float(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum / count)
    
main()
