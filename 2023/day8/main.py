from collections import Counter
import math


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def create_node_map(steps: list[str]):
    nodes = {}
    for step in steps:
        node, lr = step.replace(" ", "").split("=")
        l, r = lr.replace("(", "").replace(")", "").split(",")
        nodes[node] = {"L": l, "R": r}
    return nodes


def part1(input: list[str]):
    commands = list(input[0])
    steps = input[2:]
    nodes = create_node_map(steps)
    steps_taken = 0
    curr_node = "AAA"
    i = 0
    while True:
        steps_taken += 1
        new_node = nodes[curr_node][commands[i]]
        if new_node == "ZZZ":
            break
        i += 1
        if i > len(commands) - 1:
            i = 0
        curr_node = new_node
    print(steps_taken)


def part2(input):
    commands = list(input[0])
    steps = input[2:]
    nodes = create_node_map(steps)
    end_a = list(filter(lambda x: x[-1] == "A", nodes))
    steps_taken = [0] * len(end_a)
    curr_nodes = end_a.copy()
    dones = [False] * len(end_a)
    i = 0
    l = 0
    print(end_a)
    i = 0
    steps_taken = 0
    steps_takens = [0] * len(end_a)
    for idx, curr_node in enumerate(curr_nodes):
        while True:
            steps_taken += 1
            new_node = nodes[curr_node][commands[i]]
            if new_node[-1] == "Z":
                break
            i += 1
            if i > len(commands) - 1:
                i = 0
            curr_node = new_node
        steps_takens[idx] = steps_taken
    print(math.lcm(*steps_takens))
    return


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
