import re

with open("input.txt", "r") as data:
    instruction_list = [row.strip() for row in data]

def part1():
    grid = [[False] * 1000 for _ in range(1000)]

    def turn_off(grid, from_co, to_co):
        for row in range(from_co[0], to_co[0] + 1):
            for col in range(from_co[1], to_co[1] + 1):
                grid[row][col] = False

    def turn_on(grid, from_co, to_co):
        for row in range(from_co[0], to_co[0] + 1):
            for col in range(from_co[1], to_co[1] + 1):
                grid[row][col] = True

    def toggle(grid, from_co, to_co):
        for row in range(from_co[0], to_co[0] + 1):
            for col in range(from_co[1], to_co[1] + 1):
                grid[row][col] = not grid[row][col]

    for instruction in instruction_list:
        match = re.search(r'(\d+),(\d+) through (\d+),(\d+)', instruction)
        if match:
            from_co = (int(match.group(1)), int(match.group(2)))
            to_co = (int(match.group(3)), int(match.group(4)))

            if "turn on" in instruction:
                turn_on(grid, from_co, to_co)
            elif "turn off" in instruction:
                turn_off(grid, from_co, to_co)
            elif "toggle" in instruction:
                toggle(grid, from_co, to_co)

    count = 0
    for row in grid:
        for cell in row:
            if cell:
                count += 1

    print(f"Lights on: {count}")

def part2():
    grid = [[0] * 1000 for _ in range(1000)]

    def turn_off(grid, from_co, to_co):
        for row in range(from_co[0], to_co[0] + 1):
            for col in range(from_co[1], to_co[1] + 1):
                if grid[row][col] > 0:
                    grid[row][col] -= 1

    def turn_on(grid, from_co, to_co):
        for row in range(from_co[0], to_co[0] + 1):
            for col in range(from_co[1], to_co[1] + 1):
                grid[row][col] += 1

    def toggle(grid, from_co, to_co):
        for row in range(from_co[0], to_co[0] + 1):
            for col in range(from_co[1], to_co[1] + 1):
                grid[row][col] += 2

    for instruction in instruction_list:
        match = re.search(r'(\d+),(\d+) through (\d+),(\d+)', instruction)
        if match:
            from_co = (int(match.group(1)), int(match.group(2)))
            to_co = (int(match.group(3)), int(match.group(4)))

            if "turn on" in instruction:
                turn_on(grid, from_co, to_co)
            elif "turn off" in instruction:
                turn_off(grid, from_co, to_co)
            elif "toggle" in instruction:
                toggle(grid, from_co, to_co)

    print(f"Sum of brightness: {sum(sum(row) for row in grid)}")

part1()
part2()

