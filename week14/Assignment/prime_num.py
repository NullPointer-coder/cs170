# Jingbo Wang
# prime_num.py
# A program to find the prime numbers between 3 and input value

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
    print("The program to find the prime numbes between 3 and n.")
    # get input by user if number > 2
    while True:
         number = int(input("Please enter the number to check:"))
         if number > 2:
              break
         print("Input number large than 2! Try agin!") 
    
    # create a empty list to store prime_number
    prime_num_list = []
    
    # check every number through 3 to the number user typed
    for n in range(3, number + 1):
        # to check the number is prime or not
        if is_prime(n) == math.ceil(math.sqrt(n)) and n != 4:
            # if it is a prime number, then store it into the list
            prime_num_list.append(n)
    print("prime number between 3 and "+ str(number) + " is: \n", *prime_num_list)

main()
