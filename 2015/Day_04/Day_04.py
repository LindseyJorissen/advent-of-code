import hashlib

def part1():
    secretkey = "bgvyzdsv"
    number = 0

    while True:
        test_code = secretkey + str(number)
        result = hashlib.md5(test_code.encode()).hexdigest()

        if result[:5] == "00000":
            print(f"Found it! Number: {number}")
            print(f"Hash: {result}")
            break
        number += 1

def part2():
    secretkey = "bgvyzdsv"
    number = 0

    while True:
        test_code = secretkey + str(number)
        result = hashlib.md5(test_code.encode()).hexdigest()

        if result[:6] == "000000":
            print(f"Found it! Number: {number}")
            print(f"Hash: {result}")
            break
        number += 1

part1()
part2()
