""" Advent of Code Day 1 - Pair up the smallest number in the left list with the smallest number in the right list.
Within each pair, figure out how far apart the two numbers are
and add up all of those distances."""

def read_input_file(filename):
    """read inputfile with puzzle input, return two lists. One for the left and one for the right column. """
    left_column = []
    right_column = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            left, right = line.strip().split()
            left_column.append(int(left))
            right_column.append(int(right))
    return left_column, right_column

def calculate_differences(left_column, right_column):
    """"Sort both input lists and return the sum of the difference between the nth numbers"""
    left_column.sort()
    right_column.sort()
    difference = 0
    for i in range(len(left_column)):
        if left_column[i] >= right_column[i]:
            difference += (left_column[i] - right_column[i])
        else:
            difference += (right_column[i] - left_column[i])
    return difference

def main():
    input_file = "input.txt"
    left_column, right_column = read_input_file(input_file)
    difference = calculate_differences(left_column, right_column)
    print(f"Part 1 : {difference}")

main()
    