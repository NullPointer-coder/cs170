# average1.py
# Jingbo Wang
# A program to average a set of numbers
# Illustrates counted loop with accumulator

def main():
    n = int(input("How many numbers do you have?"))
    sum = 0.0
    for i in range(n):
        x = float(input("Enter a number >> "))
        sum = sum + x
    print("\nThe average of the numbers is", sum / n)

main()
