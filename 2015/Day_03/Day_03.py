instruction_list = []
with open("input.txt", "r") as data:
    instruction_list = list(data.read().strip())
def part1():
    houses_coor = [(0, 0)]
    for i in instruction_list:
        old_spot = houses_coor[-1]
        if i == ">":
            new_spot = (old_spot[0] + 1, old_spot[1])
        elif i == "<":
            new_spot = (old_spot[0] - 1, old_spot[1])
        elif i == "v":
            new_spot = (old_spot[0], old_spot[1] - 1)
        elif i == "^":
            new_spot = (old_spot[0], old_spot[1] + 1)
        houses_coor.append(new_spot)
    unique_houses = set(houses_coor)
    print(f"Part 1: {len(unique_houses)}")

def part2():
    santa_inst = []
    robot_inst = []
    for index,inst in enumerate(instruction_list):
        if index % 2 == 0:
            santa_inst.append(inst)
        else:
            robot_inst.append(inst)

    houses_coor = [(0, 0)]
    for i in santa_inst:
        old_spot = houses_coor[-1]
        if i == ">":
            new_spot = (old_spot[0] + 1, old_spot[1])
        elif i == "<":
            new_spot = (old_spot[0] - 1, old_spot[1])
        elif i == "v":
            new_spot = (old_spot[0], old_spot[1] - 1)
        elif i == "^":
            new_spot = (old_spot[0], old_spot[1] + 1)
        houses_coor.append(new_spot)

    houses_coor2 = [(0, 0)]
    for j in robot_inst:
        old_spot = houses_coor2[-1]
        if j == ">":
            new_spot = (old_spot[0] + 1, old_spot[1])
        elif j == "<":
            new_spot = (old_spot[0] - 1, old_spot[1])
        elif j == "v":
            new_spot = (old_spot[0], old_spot[1] - 1)
        elif j == "^":
            new_spot = (old_spot[0], old_spot[1] + 1)
        houses_coor2.append(new_spot)
    joined_list = houses_coor +houses_coor2
    unique_houses = set(joined_list)
    print(f"Part 2: {len(unique_houses)}")


part1()
part2()
