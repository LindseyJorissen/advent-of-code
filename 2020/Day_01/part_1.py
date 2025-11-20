import math
def read_input_file(filename):
    """read inputfile with puzzle input and return a list of strings containing each line"""
    entries = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            entries.append(int(line.strip()))
    return entries

def find_result(entries,sum_result):
    mul_entries = []
    for entry in entries:
        if str(sum_result - int(entry)) in entries:
            mul_entries.append(int(entry))
    return mul_entries

entries_list = read_input_file("input.txt")
mul_entries = find_result(entries_list,2020)
print(math.prod(mul_entries))


