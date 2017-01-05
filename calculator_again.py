"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic_again import *

# Your code goes here


def calculate():
    """Make basic prefix calculations.

    This calculator can add, subtract, multiply,
    or divide two numbers. It can also square a number,
    cube a number, raise a number to an exponent, and
    find a remainder when dividing two numbers.
    """

    while True:
        user_input = raw_input(">  ")
        nums = user_input.split(" ")
        if nums[0] == "q" or nums[0] == "Q":
            break
        elif nums[0] == "+":
            print add()
        elif nums[0] == "-":
            print add()
        elif nums[0] == "*":
            print multiply()
        elif nums[0] == "/":
            print divide()
        elif nums[0] == "square":
            print square()
        elif nums[0] == "cube":
            print cube()
        elif nums[0] == "power":
            print power()
        elif nums[0] == "mod":
            print mod()

calculate()
