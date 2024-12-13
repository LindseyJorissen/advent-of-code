"""Advent of Code Day 3 - Look though inputfile and find mul(x,y) within corrupted data.
Multiply X*Y and add result in a total, for part 2: start ignoring mul's when don't() is encountered"""
import re
def read_input_file(inputfile):
    """read inputfile with puzzle input and return a long string containing each line"""
    with open(inputfile, "r") as inputfile:
        return inputfile.read()

def find_valid_mul(input):
    """using regular expression (re) to find all mul(X,Y) patterns in string. Also do() and don't().
    and returns a list of all matching patterns"""
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)",input)

def find_multiplications(expressions):
    """Goes through list of muls and do()/don't() statements and multiplies the ints"""
    total = 0
    for i in expressions:
        if i[0]=="m":
            nums = list(map(int, re.findall(r'\d{1,3}', i)))
            total += nums[0] * nums[1]
    return total

def multiplications_if_do(expressions):
    """Checks if next expression is a do() or don't() and multiply muls if True"""
    total = 0
    do_enabled = True
    for i in expressions:
        if i == "do()":
            do_enabled = True
        elif i == "don't()":
            do_enabled = False
        elif do_enabled and i.startswith("m"):
            nums = list(map(int, re.findall(r'\d{1,3}', i)))
            total += nums[0] * nums[1]
    return total


def main():
    inputfile = "input.txt"
    input = read_input_file(inputfile)
    expressions = find_valid_mul(input)

    part1 = find_multiplications(expressions)
    part2 = multiplications_if_do(expressions)

    print(f"Part 1: {part1}\nPart 2: {part2}")


main()
