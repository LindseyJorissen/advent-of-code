import re

with open("input.txt","r") as data:
    gift_list = [line.strip() for line in data]

def part1():
    total_squarefeet = 0
    for gift in gift_list:
        numbers = re.split("x",gift)
        l = int(numbers[0])
        w = int(numbers[1])
        h = int(numbers[2])
        smallest_number = min(l*w, w*h, h*l)
        sum_of_package = (2 * (l * w)) + (2 * (w * h)) + (2 * (h * l)) + smallest_number
        total_squarefeet += sum_of_package
    print(f"Part 1: {total_squarefeet}")

def part2():
    total_ribbon_needed = 0
    for gift in gift_list:
        numbers = re.split("x",gift)
        l = int(numbers[0])
        w = int(numbers[1])
        h = int(numbers[2])
        ribbon_bow = l*w*h
        biggest_number = max(l,w,h)
        numbers.remove(str(biggest_number))
        a = int(numbers[0])
        b = int(numbers[1])
        ribbon_wrap = a + a + b + b
        gift_ribbon_needed = ribbon_wrap+ribbon_bow
        total_ribbon_needed +=gift_ribbon_needed
    print(f"Part 2: {total_ribbon_needed}")
part1()
part2()