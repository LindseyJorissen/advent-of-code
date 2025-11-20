from part_1 import read_input_file

def find_result(entries,sum_result):
    mul_entries = []
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            a = entries[i]
            b = entries[j]
            c = 2020 - a - b
            if c in entries[j+1:]:
                print(a, b, c, a*b*c)


entries_list = read_input_file("input.txt")
mul_entries = find_result(entries_list,2020)
