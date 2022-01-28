# Jingbo Wang
# factorial.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator

def main():
    # input a number which needs to factor
    n = eval(input("Please enter a whole number: "))
    fact = 1
    
    for factor in range(n,1,-1):
       # calculate n!
       fact = fact * factor
    print("The factorial of", n, "is", fact)

main()
