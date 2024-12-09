def read_input_file(filename):
    reports = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            reports.append(line.strip())
    return reports

def is_safe(reports):
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