from calculator_again import *


def add(nums):

    total = 0
    for num in nums:
        total += num
    return total


def subtract(nums):

    total = nums[1]
    for num in nums:
        total -= num
    return total


def multiply(nums):

    total = 1
    for num in nums:
        total *= num
    return total


def divide(nums):
    # Need to turn at least argument to float for division to
    # not be integer division
    total = float(nums[1])
    for num in nums:
        total /= num
    return total


def square(nums):
    # Needs only one argument
    total = []
    for num in nums:
        total.append(num * num)
    return total


def cube(nums):
    # Needs only one argument
    total = []
    for num in nums:
        total.append(num * num * num)
    return total


def power(nums):

    total = []
    for num in nums:
        total **= num
    return total  # ** = exponent operator


def mod(nums):

    total = nums[1]
    for num in nums:
        total %= num
    return total
