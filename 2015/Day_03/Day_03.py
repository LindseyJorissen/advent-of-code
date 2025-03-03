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

    for index, inst in enumerate(instruction_list):
        if index % 2 == 0:
            santa_inst.append(inst)
        else:
            robot_inst.append(inst)

    santa_start_pos= (0, 0)
    robot_start_pos = (0, 0)
    visited_houses = {(0, 0)}

    for i in santa_inst:
        if i == ">":
            santa_start_pos = (santa_start_pos[0] + 1, santa_start_pos[1])
        elif i == "<":
            santa_start_pos = (santa_start_pos[0] - 1, santa_start_pos[1])
        elif i == "v":
            santa_start_pos = (santa_start_pos[0], santa_start_pos[1] - 1)
        elif i == "^":
            santa_start_pos = (santa_start_pos[0], santa_start_pos[1] + 1)
        visited_houses.add(santa_start_pos)

    for j in robot_inst:
        if j == ">":
            robot_start_pos = (robot_start_pos[0] + 1, robot_start_pos[1])
        elif j == "<":
            robot_start_pos = (robot_start_pos[0] - 1, robot_start_pos[1])
        elif j == "v":
            robot_start_pos = (robot_start_pos[0], robot_start_pos[1] - 1)
        elif j == "^":
            robot_start_pos = (robot_start_pos[0], robot_start_pos[1] + 1)
        visited_houses.add(robot_start_pos)

    print(f"Part 2: {len(visited_houses)}")


part1()
part2()
