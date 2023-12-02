import re


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def find_first(string: str):
    for i in range(len(string)):
        if string[i].isdigit():
            return (str(string[i]), i)
    return ("0", -1)


def find_first_str(string, rev=False):
    nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    first = 1e10
    actual = 0
    for k, v in nums.items():
        rst = re.search(k[::-1] if rev else k, string)
        if rst and rst.start() < first:
            first = rst.start()
            actual = v
    rst2 = find_first(string)
    if rst2[1] != -1 and rst2[1] <= first:
        return str(rst2[0])
    return str(actual)


def part1(input):
    return sum([int(find_first(i)[0] + find_first(i[::-1])[0]) for i in input])


def part2(input):
    return sum([int(find_first_str(i) + find_first_str(i[::-1], True)) for i in input])


def main():
    input = read_file("input.file")
    print("-----------------")
    print("Running part 1...")
    print(part1(input))
    print("-----------------")
    print("Running part 2...")
    print(part2(input))
    print("-----------------")


main()
