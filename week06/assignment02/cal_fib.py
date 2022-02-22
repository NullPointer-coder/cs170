# Jingbo Wang
# This program is to show A Fibonacci sequence is a sequence
# of numbers where each successive number is the sum of the previous two,
# and sum A list of Fibonacci sequence is a sequence of numbers
# where each successive number is the sum of the previous two.

from unittest import result


def fib(n):
  if n <= 0:
    return 0;
  elif n == 1:
    return 1
  else:
    return (fib(n - 1) + fib(n - 2))

def sum_fib(n):
    sum = 0
    result_list = [ ]
    for i in range(1, n + 1):
      result_list.append(fib(i))
    for index in range(n):
      sum += result_list[index]
    return sum

def main():
    print("A Fibonacci sequence is a sequence of numbers where each"
             +" successive number is the sum of the previous two.")
    n = int(input("Please enter a number: "))
    result = fib(n)
    print("result: ", result)
    
    print("A Fibonacci sequence is a sequence of numbers where each"
             +" successive number is the sum of the previous two.")
    n = int(input("Please enter a number: "))
    sum = sum_fib(n)
    print("result: ", sum)


main()
