"""Advent of Code Day 3 - Look though inputfile and find mul(x,y) within corrupted data.
Multiply X*Y and add result in a total """

def read_input_file(filename):
    """read inputfile with puzzle input and return a list of strings containing each line"""
    input = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            input.append(line)
    return input

def find_mul(input):
    """loop through lines of input to find 'mul' in the form 'mul(x, y)'.
    Save 'x' and 'y' from each 'mul' operation, store them in a list,
    and calculate their multiplication sum."""
    total = 0
    for line in input:
        i = 0
        while i < len(line):

            if line[i:i + 4] == "mul(":
                j = i + 4 # -> Start searching after mul(, j = new index

                while j < len(line) and line[j] != ')': # -> increase index j by 1 until ) is found
                    j += 1

                if j < len(line):
                    parameters= line[i + 4:j].strip() # -> Strips string "X,Y"
                    individual_x_y = parameters.split(',') # -> ["X","Y"]

                    if len(individual_x_y) == 2 and individual_x_y[0].isdigit() and individual_x_y[1].isdigit():
                        x, y = int(individual_x_y[0]), int(individual_x_y[1])
                        total += x * y
                i += 4
            else:
                i += 1
    return total

def main():
    filename = "input.txt"
    input = read_input_file(filename)
    if input:
        total = find_mul(input)
        print("Total Part 1:", total)
main()