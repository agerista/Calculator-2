def add(nums_list):

    total = 0
    for num in nums_list:
        total += num
    return total


def subtract(nums_list):

    total = nums_list[1]
    for num in nums_list:
        total -= num
    return total


def multiply(nums_list):

    total = 1
    for num in nums_list:
        total *= num
    return total


def divide(nums_list):
    # Need to turn at least argument to float for division to
    # not be integer division
    total = float(nums_list[1])
    for num in nums_list:
        total /= num
    return total


def square(nums_list):
    # Needs only one argument
    total = []
    for num in nums_list:
        total.append(num * num)
    return total


def cube(nums_list):
    # Needs only one argument
    total = []
    for num in nums_list:
        total.append(num * num * num)
    return total


def power(nums_list):

    total = []
    for num in nums_list:
        total **= num
    return total  # ** = exponent operator


def mod(nums_list):

    total = nums_list[1]
    for num in nums_list:
        total %= num
    return total
