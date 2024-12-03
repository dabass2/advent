def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def part1(input):
    return


def part2(input):
    return


def main():
    input = read_file("test.file")
    print("-----------------")
    print("Running part 1...")
    part1(input)
    print("-----------------")
    print("Running part 2...")
    part2(input)
    print("-----------------")


main()
