def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def strictly_increasing(L):
    return all(x < y and abs(x - y) <= 3 for x, y in zip(L, L[1:]))


def strictly_decreasing(L):
    return all(x > y and abs(x - y) <= 3 for x, y in zip(L, L[1:]))


def strictly_monotonic(L):
    return strictly_increasing(L) or strictly_decreasing(L)


def part1(reports):
    readings = sum(
        [
            strictly_monotonic(y)
            for y in [[int(x) for x in report.split()] for report in reports]
        ]
    )
    print(readings)


def part2(reports):
    totalSafe = 0
    readings = [y for y in [[int(x) for x in report.split()] for report in reports]]
    for reading in readings:
        safe = False
        if not strictly_monotonic(reading):
            for i in range(0, len(reading)):
                if strictly_monotonic(reading[:i] + reading[i + 1 :]):
                    safe = True
        else:
            safe = True
        totalSafe += 1 if safe else 0
    print(totalSafe)


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
