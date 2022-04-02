# primenum_check.py
# Jingbo Wang
# find out if a number is prime or not

import math

def main():
    print("finds if a number is prime ot not...")

    # get input number
    n = int(input("enter a number to be checked for primelity: "))
    counter = 2 # goes from 2 -> ceil(n/2)
    while counter < math.ceil(n/2):
        if n % counter == 0:
            break # the number got divided, no point continuing
        
        counter += 1

    if counter == math.ceil(n/2): # upper bound check
        print("prime")
    else:
        print("not a prime")
main()
        
