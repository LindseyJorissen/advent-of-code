instruction_list = []
with open("input.txt","r") as data:
    instruction_list = list(data.read())


def part1():
    current_floor = 0
    for char in instruction_list:
        if char == "(":
            current_floor +=1
        elif char == ")":
            current_floor -=1
    print(f"Part 1: {current_floor}")

def part2():
    current_floor = 0
    for index, char in enumerate(instruction_list, start=1):
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1
        if current_floor < 0:
            print(f"Part 2: {index}")
            break

part1()
part2()
