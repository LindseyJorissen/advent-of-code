def read_input_file(filename):
    reports = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            reports.append(line.strip())
    return reports

def safety_check(reports):
    safety_check_list = [False] * len(reports)
    for i in range(len(reports)):
        check_counter = 0
        test_list = reports[i].split()
        int_list = list(map(int, test_list))
        if int_list == sorted(int_list) or int_list == sorted(int_list, reverse=True):
            check_counter += 1
        if check_counter == 0:
            continue
        else:
            for j in range(len(int_list) - 1):
                diff = int_list[j+1] - int_list[j]
                if (1 <= diff <= 3 or -3 <= diff <= -1):
                    continue
                else:
                    break
            else:
                safety_check_list[i] = True
    return safety_check_list

def main():
    filename = "input.txt"
    reports = read_input_file(filename)
    safety_check_list = safety_check(reports)
    safecounter = sum(safety_check_list)
    print(safecounter)

main()






