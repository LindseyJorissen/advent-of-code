"""Advent of Code Day 1 - Calculate a 'similarity score' by counting how often each number from the left list
appears in the right list and summing the products of each number in the left list with
its occurrence amount in the right list."""

from part_1 import read_input_file

def count_occurrence(left_column, right_column):
    """read inputfile with puzzle input, and return a dictionary where keys are numbers from the left column
    and values are the counts of their occurrences in the right column."""
    occurrence = {}
    for i in range(len(left_column)):
       occurrence.update({left_column[i]: right_column.count(left_column[i])})
    return occurrence

def calc_similarity_score(occurrence):
    """Calculate the 'similarity score' by summing the product of each number in the left
    column and its occurrence count from the right column."""
    similarity_score = 0
    for key, value in occurrence.items():
        similarity_score += (key * value)
    return similarity_score

def main():
    input_file = "input.txt"
    left_column, right_column = read_input_file(input_file)
    occurrence = count_occurrence(left_column, right_column)
    similarity_score = calc_similarity_score(occurrence)
    print(f"Part 2 : {similarity_score}")

main()

