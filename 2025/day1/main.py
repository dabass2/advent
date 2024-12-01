from collections import Counter


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def part1(input):
    left, right = list(zip(*[pair.split("   ") for pair in input]))
    left = sorted(left)
    right = sorted(right)
    distances = []
    for i in range(0, len(left)):
        distances.append(abs(int(left[i]) - int(right[i])))
    print(sum(distances))


def part2(input):
    left, right = list(zip(*[pair.split("   ") for pair in input]))
    rightMap = Counter(right)
    simScore = sum([int(rightMap[x]) * int(x) for x in left])
    print(simScore)


def main():
    input = read_file("input.file")
    print("-----------------")
    print("Running part 1...")
    part1(input)
    print("-----------------")
    print("Running part 2...")
    part2(input)
    print("-----------------")


main()
