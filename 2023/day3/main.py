import re


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


ALL_AROUND = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def check_neighbors(grid: list[str], start_idx: tuple[int, int]) -> bool:
    x, y = start_idx
    for neighbor_x, neighbor_y in ALL_AROUND:
        new_x, new_y = x + neighbor_x, y + neighbor_y

        IS_X_VALID: bool = new_x >= 0 and new_x < len(grid)
        IS_Y_VALID: bool = new_y >= 0 and new_y < len(grid[0])
        if (
            IS_X_VALID
            and IS_Y_VALID
            and (grid[new_x][new_y] != "." and not grid[new_x][new_y].isdigit())
        ):
            return True
    return False


def part1(input: list[str]):
    total = []
    for line_num, line in enumerate(input):
        num_grps = [(m.span(), int(m.group())) for m in re.finditer("\d+", line)]
        for grp_span, grp_val in num_grps:
            for i in range(*grp_span):
                if check_neighbors(input, (line_num, i)):
                    total.append(grp_val)
                    break
    print(sum(total))
    return


def part2(input):
    total = 0
    for line_num, line in enumerate(input):
        gear_grps = [(m.start(), m.group()) for m in re.finditer("\*+", line)]
        for gear_grp_pos, gear in gear_grps:
            num_grps = [(m.span(), m.group()) for m in re.finditer("\d+", line)]
            if line_num - 1 >= 0:
                num_grps += [
                    (m.span(), m.group())
                    for m in re.finditer("\d+", input[line_num - 1])
                ]
            if line_num + 1 < len(input):
                num_grps += [
                    (m.span(), m.group())
                    for m in re.finditer("\d+", input[line_num + 1])
                ]

            neighbors: list[int] = []
            for num_grp_span, num in num_grps:
                if gear_grp_pos in range(num_grp_span[0] - 1, num_grp_span[1] + 1):
                    neighbors.append(int(num))
            if len(neighbors) == 2:
                total += neighbors[0] * neighbors[1]
    print(total)
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
