"""Advent of Code Day 2 - Introducing a new condition:
Attempt to make unsafe reports safe by removing one integer from each report."""
from part_1 import read_input_file,is_safe

def can_become_safe_by_removing_one(unsafe_reports):
    """ Attempt to convert unsafe reports into safe ones by removing one integer from each report.
    And returning an updated safe-list"""
    updated_safe_reports = []
    for report in unsafe_reports:
        found_safe = False
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if len(modified_report) > 1:
                if ( modified_report == sorted(modified_report) and \
                    all(1 <= modified_report[j + 1] - modified_report[j] <= 3 for j in range(len(modified_report) - 1))) or \
                    modified_report == sorted(modified_report, reverse=True) and \
                    all(1 <= modified_report[j] - modified_report[j + 1] <= 3 for j in range(len(modified_report) - 1)):
                    updated_safe_reports.append(modified_report)
                    found_safe = True
                    break
    return updated_safe_reports

def main():
    filename = "input.txt"
    reports = read_input_file(filename)
    unsafe_reports = is_safe(reports)
    updated_safe_reports= can_become_safe_by_removing_one(unsafe_reports)
    print(f"Part 2: New amount of safe reports: {len(updated_safe_reports)}")

main()
