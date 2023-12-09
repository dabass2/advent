from collections import Counter


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def score_hands(games: list[list[str]]):
    scored_hands = [[] for _ in range(7)]
    for game in games:
        counted_game = Counter(game[0])
        vals = sorted(list(counted_game.values()))
        idx = 0
        if len(vals) == 1:  # five of a kind
            idx = 6
        elif len(vals) == 2 and vals[1] == 4:  # four of a kind
            idx = 5
        elif len(vals) == 2 and vals[1] == 3:  # full house
            idx = 4
        elif len(vals) == 3 and vals[2] == 3:  # three of a kind
            idx = 3
        elif len(vals) == 3 and vals[1] == 2 and vals[2] == 2:  # two pair
            idx = 2
        elif len(vals) == 4:  # one pair
            idx = 1
        else:  # high card
            idx = 0
        scored_hands[idx].append(game)
    return scored_hands


def score_hands_2(games: list[list[str]]):
    scored_hands = [[] for _ in range(7)]
    for game in games:
        counted_game = Counter(game[0])
        print(game)
        print(counted_game["J"])
        vals = sorted(list(counted_game.values()))
        print(vals)
        idx = 0
        if len(vals) == 1 or (
            len(vals) == 2
            and vals[1] == 4
            and counted_game["J"] == 1
            or len(vals) == 2
            and vals[1] == 3
            and counted_game["J"] == 2
            or len(vals) == 2
            and vals[1] == 2
            and counted_game["J"] == 3
            or len(vals) == 2
            and vals[1] == 1
            and counted_game["J"] == 2
        ):  # five of a kind
            idx = 6
        elif (
            len(vals) == 2
            and vals[1] == 4
            or (len(vals) == 3 and counted_game["J"] == 1 and vals[2] == 3)
            or (len(vals) == 3 and counted_game["J"] == 2 and vals[2] == 2)
            or (len(vals) == 3 and counted_game["J"] == 3 and vals[2] == 1)
        ):  # four of a kind
            idx = 5
        elif len(vals) == 2 and vals[1] == 3:  # full house
            idx = 4
        elif len(vals) == 3 and vals[2] == 3:  # three of a kind
            idx = 3
        elif len(vals) == 3 and vals[1] == 2 and vals[2] == 2:  # two pair
            idx = 2
        elif len(vals) == 4:  # one pair
            idx = 1
        else:  # high card
            idx = 0
        scored_hands[idx].append(game)
    print(scored_hands)
    return scored_hands


def sort_fn(string1: str, string2: str, pt2=False):
    SORT_KEY = {"A": 14, "K": 13, "Q": 12, "J": 1 if pt2 else 11, "T": 10}
    for idx in range(len(string1)):
        if string1[idx] == string2[idx]:
            continue
        string1_val = (
            SORT_KEY[string1[idx]] if string1[idx] in SORT_KEY else int(string1[idx])
        )
        string2_val = (
            SORT_KEY[string2[idx]] if string2[idx] in SORT_KEY else int(string2[idx])
        )
        # print(string1_val, string2_val)
        return string1_val > string2_val
        # if string1_val > string2_val:
        #     return string1
        # else:
        #     return string2


def bubbleSort(arr, pt2=False):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # print(
            #     f"Comparing: {arr[j][0]} and {arr[j + 1][0]}. Result: {sort_fn(arr[j][0], arr[j + 1][0])}"
            # )
            if sort_fn(arr[j][0], arr[j + 1][0], pt2):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


def part1(input: list[str]):
    hands = [i.split(" ") for i in input]
    scored_hands = score_hands(hands)
    rank = 0
    total = 0
    for score in scored_hands:
        bubbleSort(score)
        for _, bid in score:
            rank += 1
            total += int(bid) * rank
    print(total)


def part2(input):
    hands = [i.split(" ") for i in input]
    scored_hands = score_hands_2(hands)
    rank = 0
    total = 0
    for score in scored_hands:
        bubbleSort(score, pt2=True)
        for _, bid in score:
            rank += 1
            # print(_, bid, rank)
            total += int(bid) * rank
    print(total)


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
