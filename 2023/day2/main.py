def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def part1(input: list[str]):
    MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14
    valid_games: list[int] = []
    for game in input:
        game_info, all_pulls = game.split(":")
        game_id = game_info.split(" ")[1]
        reds: int = 0
        blues: int = 0
        greens: int = 0
        for pulls in all_pulls.split(";"):
            for pull in pulls.strip().split(", "):
                num_pulled, color = pull.split(" ")
                num_pulled = int(num_pulled)
                if color == "red" and num_pulled > reds:
                    reds = num_pulled
                if color == "blue" and num_pulled > blues:
                    blues = num_pulled
                if color == "green" and num_pulled > greens:
                    greens = num_pulled
        if reds <= MAX_RED and blues <= MAX_BLUE and greens <= MAX_GREEN:
            valid_games.append(int(game_id))
    return sum(valid_games)


def part2(input: list[str]):
    powers: list[int] = []
    for game in input:
        _, all_pulls = game.split(":")
        reds: int = 0
        blues: int = 0
        greens: int = 0
        for pulls in all_pulls.split(";"):
            for pull in pulls.strip().split(", "):
                num_pulled, color = pull.split(" ")
                num_pulled = int(num_pulled)
                if color == "red" and num_pulled > reds:
                    reds = num_pulled
                if color == "blue" and num_pulled > blues:
                    blues = num_pulled
                if color == "green" and num_pulled > greens:
                    greens = num_pulled
        powers.append(reds * greens * blues)
    print(sum(powers))


def main():
    input = read_file("input.file")
    # print("-----------------")
    # print("Running part 1...")
    # print(part1(input))
    print("-----------------")
    print("Running part 2...")
    part2(input)
    print("-----------------")


main()
