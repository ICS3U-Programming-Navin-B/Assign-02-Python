#!/usr/bin/env python3
# Created by: Navin Baleko
# Created on: Dec 2, 2021
# This program asks the user for the length of a cube
# It then calculates the volume and surface area and a cube
import math

def main():
    # input
    print("Today we will calculate the volume and")
    print("surface area of a cube")
    length = int(input("Enter the length (cm): "))
    
    # process
    volume = length**3
    surface_area = 6 *(length**2)

    # output
    print("")
    print ("Volume = {} cm^3". format (volume))
    print ("Surface Area = {} cm^2". format (surface_area))


if __name__ == "__main__":
  main()