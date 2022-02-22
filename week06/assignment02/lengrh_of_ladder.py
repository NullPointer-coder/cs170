# Jingbo Wang
# This program to determine the length of a ladder
# required to reach a given height when leaned against a house.

import math

def main():
  print(" to determine the length of a ladder "
           + "required to reach a given height when leaned against a house.")
  # get height and angle
  height = int(input("Please enter the height: "))
  angle = int(input("Please enter the angle degree of ladder: "))

 # turn angle to radians
  radians = angle * (math.pi / 180)

  # calculate the ladder length
  length = height / math.sin(radians)
  print("The length of a ladder required is", length)

main()
