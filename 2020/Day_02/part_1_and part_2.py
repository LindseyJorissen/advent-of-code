def check_password_validity(filename):
  valid = 0
  valid_2 = 0
  with open("input.txt") as file:
        for line in file:
            policy, letter_with_colon, password = line.split()
            min_count, max_count = map(int, policy.split("-"))
            letter = letter_with_colon[0]

            if min_count <= password.count(letter) <= max_count:
                valid += 1

            index_1, index_2 = map(int, policy.split("-"))
            if index_1-1 < len(password) and index_2-1 < len(password):
                if (password[index_1-1] == letter) ^ (password[index_2-1] == letter):
                    valid_2 += 1
        return valid,valid_2



filename = "input.txt"
valid, valid_2 = check_password_validity(filename)
print(f"part 1: {valid}\npart 2: {valid_2}")