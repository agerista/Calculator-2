"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculate():
    """Make basic prefix calculations.

    This calculator can add, subtract, multiply,
    or divide two numbers. It can also square a number,
    cube a number, raise a number to an exponent, and
    find a remainder when dividing two numbers.
    """

    while True:
        calculation = raw_input(">  ")
        nums = calculation.split(" ")
        if nums[0] == "q" or nums[0] == "Q":
            break
        elif nums[0] == "+":
            print add(int(nums[1]), int(nums[2]))
        elif nums[0] == "-":
            print add(int(nums[1]), int(nums[2]))
        elif nums[0] == "*":
            print multiply(int(nums[1]), int(nums[2]))
        elif nums[0] == "/":
            print divide(float(nums[1]), float(nums[2]))
        elif nums[0] == "square":
            print square(int(nums[1]))
        elif nums[0] == "cube":
            print cube(int(nums[1]))
        elif nums[0] == "power":
            print power(int(nums[1]), int(nums[2]))
        elif nums[0] == "mod":
            print mod(int(nums[1]), int(nums[2]))

calculate()
