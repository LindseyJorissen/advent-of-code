def read_input_file(filename):
    input = []
    with open(filename, "r") as inputfile:
        for line in inputfile:
            input.append(line)
    return input

def find_mul(input):
    results = []
    total = 0
    for line in input:
        i = 0
        while i < len(line):
            if line[i:i + 4] == "mul(":
                j = i + 4
                while j < len(line) and line[j] != ')':
                    j += 1
                if j < len(line):
                    params = line[i + 4:j].strip()
                    parts = params.split(',')
                    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                        x, y = int(parts[0]), int(parts[1])
                        results.append((x, y))
                        total += x * y
                i += 4
            else:
                i += 1
    return results, total

def main():
    filename = "input.txt"
    input = read_input_file(filename)
    if input:
        results, total = find_mul(input)
        print("Total Part 1:", total)
main()