"""Advent of Code Day 2 -  Reads a list of reports from a file,each report contains a sequence of integers.
Check which reports are "safe" and which are "unsafe" based on 2 parameters:
1. A report is safe if its integers are sorted (ascending or descending order).
2. The difference between consecutive numbers must be between 1 and 3.
Outputs the number of safe and unsafe reports. """


def read_input_file(filename):
    """read inputfile with puzzle input and return a list of strings containing each line"""
    reports = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            reports.append(line.strip())
    return reports


def is_safe(reports):
    """Checks each level/line by the parameters, returns two lists. One for safe and one for unsafe reports"""
    safe_reports = []
    unsafe_reports = []
    for i in range(len(reports)):
        int_list = list(map(int, reports[i].split()))
        if int_list == sorted(int_list):
            if all(1 <= int_list[i + 1] - int_list[i] <= 3 for i in range(len(int_list) - 1)):
                safe_reports.append(int_list)
        if int_list == sorted(int_list, reverse=True):
            if all(1 <= int_list[j] - int_list[j + 1] <= 3 for j in range(len(int_list) - 1)):
                safe_reports.append(int_list)
        unsafe_reports.append(int_list)
    return safe_reports, unsafe_reports


def main():
    filename = "input.txt"
    reports = read_input_file(filename)
    safe_reports, unsafe_reports = is_safe(reports)
    print(f"Part 1: {len(safe_reports)} safe reports,{len(unsafe_reports)} unsafe reports ")


main()
