from typing import Union


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def part1(input: list[str]):
    history = [[int(x) for x in i.split(" ")] for i in input]
    # print(history)
    total = 0
    for scan in history:
        curr_scan = scan
        last_num = [curr_scan[-1]]
        while True:
            diffs = []
            for i in range(len(curr_scan) - 1):
                diffs.append(curr_scan[i + 1] - curr_scan[i])
            # print(diffs, diffs.count(0), len(diffs))
            last_num.append(diffs[-1])
            if len(diffs) == diffs.count(0):
                break
            curr_scan = diffs
        # print("Last num:", last_num)
        extrap_val = sum(last_num)
        # print("Extrap val:", extrap_val)
        total += extrap_val
    print(total)


def part2(input):
    history = [[int(x) for x in i.split(" ")] for i in input]
    # print(history)
    total = 0
    for scan in history:
        curr_scan = scan
        first_num = [curr_scan[0]]
        while True:
            diffs = []
            for i in range(len(curr_scan) - 1):
                diffs.append(curr_scan[i + 1] - curr_scan[i])
            # print(diffs, diffs.count(0), len(diffs))
            first_num.append(diffs[0])
            if len(diffs) == diffs.count(0):
                break
            curr_scan = diffs
        # print("First num:", first_num)
        extrap_val = 0
        for i in list(reversed(first_num)):
            extrap_val = i - extrap_val
        # print("Extrap val:", extrap_val)
        total += extrap_val
    print(total)


def main():
    input = read_file("input.file")
    # print("-----------------")
    # print("Running part 1...")
    # part1(input)
    print("-----------------")
    print("Running part 2...")
    part2(input)
    print("-----------------")


main()
