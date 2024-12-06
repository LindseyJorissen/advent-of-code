def read_input_file(filename):
    left_column = []
    right_column = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            left, right = line.strip().split()
            left_column.append(int(left))
            right_column.append(int(right))
    return left_column, right_column

def calculate_differences(left_column, right_column):
    left_column.sort()
    right_column.sort()
    difference = []
    for i in range(len(left_column)):
        if left_column[i] >= right_column[i]:
            difference.append(left_column[i] - right_column[i])
        else:
            difference.append(right_column[i] - left_column[i])
    return difference

def main():
    input_file = "input.txt"
    left_column, right_column = read_input_file(input_file)
    difference = calculate_differences(left_column, right_column)
    print(sum(difference))

main()
    