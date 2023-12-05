import functools


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def format_num_list(strings: str) -> list[int]:
    rtn = []
    for string in strings.strip().replace("  ", " ").split(" "):
        if len(string.strip()):
            rtn.append(int(string.strip()))
    return rtn


def part1(input: list[str]):
    total = 0
    for game in input:
        winning_nums, actual_nums = game.split(":")[1].split(" | ")
        winning_nums = format_num_list(winning_nums)
        actual_nums = format_num_list(actual_nums)
        rst = []
        for actual in actual_nums:
            if actual in winning_nums:
                rst.append(actual)
        local_total = 1 if len(rst) else 0
        for _ in rst[1:]:
            local_total *= 2
        total += local_total
    print(total)
    return


def part2(input: list[str]):
    all_games = input.copy()
    memory = {}
    games_seen = {}
    i = 0
    while len(all_games):
        # if i == 1:
        #     return
        if i % 1000 == 0:
            print(f"On iteration: {i} | Games left: {len(all_games)}")
        game_info, nums = all_games.pop(0).split(":")
        # all_games.pop(0)
        game_num = int(game_info.split(" ")[-1])
        # print(f"On game {game_num}")
        if game_num not in games_seen:
            games_seen[game_num] = 0
        games_seen[game_num] += 1
        winning_nums, actual_nums = nums.split(" | ")
        winning_nums = format_num_list(winning_nums)
        # print(f"Card {game_num}: {winning_nums}")
        actual_nums = format_num_list(actual_nums)
        # print(actual_nums)
        wins = 0
        if game_num in memory:
            wins = memory[game_num]
        else:
            for actual in actual_nums:
                if actual in winning_nums:
                    wins += 1
            memory[game_num] = wins
        if wins > 0:
            all_games.extend(input[game_num : game_num + wins])
        # print(game_num, wins, input[game_num : game_num + wins])
        # print(all_games, memory, games_seen)
        i += 1
        # print(f"Total wins for game: {game_num} | {memory[game_num]}")
    print(sum(games_seen.values()))
    print(memory)
    return


def main():
    input = read_file("test.file")
    # print("-----------------")
    # print("Running part 1...")
    # part1(input)
    print("-----------------")
    print("Running part 2...")
    part2(input)
    print("-----------------")


main()
