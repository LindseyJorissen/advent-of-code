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

            if modified_report == sorted(modified_report):
                sorted_ascending = True
                for j in range(len(modified_report) - 1):
                    if not (1 <= modified_report[j + 1] - modified_report[j] <= 3):
                        sorted_ascending = False
                        break

                if sorted_ascending:
                    is_safe = True
                else:
                    is_safe = False

            elif modified_report == sorted(modified_report, reverse=True):
                sorted_descending = True
                for j in range(len(modified_report) - 1):
                    if not (1 <= modified_report[j] - modified_report[j + 1] <= 3):
                        sorted_descending = False
                        break

                if sorted_descending:
                    is_safe = True
                else:
                    is_safe = False

            else:
                is_safe = False
                
            if is_safe:
                updated_safe_reports.append(modified_report)
                break
    return updated_safe_reports

def main():
    filename = "input.txt"
    reports = read_input_file(filename)
    safe_reports,unsafe_reports = is_safe(reports)
    updated_safe_reports= can_become_safe_by_removing_one(unsafe_reports)
    print(f"Part 2: New amount of safe reports: {len(updated_safe_reports)}")

main()
