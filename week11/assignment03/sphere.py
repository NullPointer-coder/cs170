# Jingbo Wang
# a program to calculate the volume and surface area of a
# sphere from its radius, given as input

import math
def sphereArea(radius):
    return  4 * math.pi * radius**2
    
def sphereVolume(radius):
    return  4 / 3 * math.pi * radius**3
    
def main():
    # get radius from user
    r = (float(input("Please enter a radius: ")))

    # print sphere area and volume
    print("sphere area is", sphereArea(r))
    print("sphere volume is", sphereVolume(r))

main()
