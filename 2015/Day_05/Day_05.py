with open("input.txt", "r") as data:
    name_list = [row.strip() for row in data]

def part1():
    naughty_list = []
    nice_list = []

    def double_letter(name):
        for i in range(len(name) - 1):
            if name[i] == name[i + 1]:
                return True
        return False

    def three_vowels(name):
        vowels = {"a", "e", "i", "o", "u"}
        vowel_counter = 0
        for letter in name:
            if letter in vowels:
                vowel_counter += 1
            if vowel_counter >= 3:
                return True
        return False

    for name in name_list:
        if "ab" in name or "cd" in name or "pq" in name or "xy" in name:
            naughty_list.append(name)
        elif double_letter(name) and three_vowels(name):
            nice_list.append(name)

    print(f"Part 1: {len(nice_list)}")

def part2():
    nice_list_2 = []
    def has_repeating_pair(name):
        for i in range(len(name) - 1):
            pair = name[i:i + 2]
            if pair in name[i + 2:]:
                return True
        return False

    def has_repeating_letter_with_gap(name):
        for i in range(len(name) - 2):
            if name[i] == name[i + 2]:
                return True
        return False

    for name in name_list:
        if has_repeating_pair(name) and has_repeating_letter_with_gap(name):
            nice_list_2.append(name)

    print(f"Part 2: {len(nice_list_2)}")
part1()
part2()