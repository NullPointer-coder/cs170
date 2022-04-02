# prime_check.py
# Jingbo Wang
# find out if a number is prime or not

import math

def main():
    print("finds if a number is prime ot not...")

    # get input number
    n = int(input("enter a number to be checked for primelity: "))

    if n == 2:
        print("prime")
    else:
        counter = 2 # goes from 2 -> ceil(sqrt(n))
        while counter < math.ceil(math.sqrt(n)):
            if n % counter == 0:
                break # the number got divided, no point continuing
            counter += 1
        if counter == math.ceil(math.sqrt(n)) and n != 4: # upper bound check
            print("prime")
        else:
            print("not a prime")
main()
        
