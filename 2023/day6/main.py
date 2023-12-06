import re


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def part1(input: list[str]):
    games = list(
        zip(*[[int(i.group()) for i in re.finditer("\d+", line)] for line in input])
    )

    num_win_mult = 1
    for time, best_dist in games:
        num_wins = 0
        for time_held in range(time):
            if time_held * (time - time_held) > best_dist:
                num_wins += 1
        num_win_mult *= num_wins if num_wins > 0 else 1
    print(num_win_mult)


def part2(input: list[str]):
    games = [
        int("".join([i.group() for i in re.finditer("\d+", line)])) for line in input
    ]

    num_win_mult = 1
    time, best_dist = games
    num_wins = 0
    for time_held in range(time):
        if time_held * (time - time_held) > best_dist:
            num_wins += 1
    num_win_mult *= num_wins if num_wins > 0 else 1
    print(num_win_mult)


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
