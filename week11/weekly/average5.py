# average5.py
# Jingbo Wang
#     Computes the average of numbers listed in a file.

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    for line in infile:
        sum = sum + float(line)
        count = count + 1
    print("\nThe average of the numbers is", sum / count)

main()
