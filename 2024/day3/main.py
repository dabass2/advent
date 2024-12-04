import re


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()[0]


def mul(cmd):
    l, r = re.findall(r"[0-9]+,[0-9]+", cmd)[0].split(",")
    return int(l) * int(r)


def part1(cmd):
    mulCmds = re.findall(r"mul\([0-9]+,[0-9]+\)", cmd)
    print(sum([mul(x) for x in mulCmds]))


def part2(cmd):
    allCmds = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", cmd)
    runCmds = True
    total = []
    for cmd in allCmds:
        action = cmd.split("(")[0]
        if action == "mul" and runCmds:
            total.append(mul(cmd))
        elif action == "don't":
            runCmds = False
        elif action == "do":
            runCmds = True
    print(sum(total))


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
