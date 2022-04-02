# prime_check2.py
# Jingbo Wang
# find out if a number is prime or not

import math
# check n is prime or not
def is_prime(n):
     counter = 2 # goes from 2 -> ceil(sqrt(n))
     while counter < math.ceil(math.sqrt(n)):
         if n % counter == 0:
            return counter
         counter += 1
     return counter

def main():
    print("finds if a number is prime ot not...")

    # get input number
    n = int(input("enter a number to be checked for primelity: "))
    if n == 2:
        print("prime")
    else:
        counter = is_prime(n)
        if counter == math.ceil(math.sqrt(n)) and n != 4: # upper bound check
            print("prime")
        else:
            print("not a prime")
main()
        
