def read_file(filename):
    with open(filename, "r") as f:
        return f.read().split("\n\n")


LOOKUP_STEPS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def create_master_dict(raw_ranges: list[str]):
    master_dict: dict[str, list[tuple[int, int, int]]] = {}
    for lookup_map in raw_ranges:
        map_name, ranges = lookup_map.split(":")
        map_name = map_name.split(" ")[0]
        ranges = ranges.strip().split("\n")
        for local_range in ranges:
            dest, src, delta = list(
                map(
                    lambda n: int(n),
                    list(map(lambda x: x.split(" "), local_range.split("\n")))[0],
                )
            )
            new_range = (src, dest, delta)
            if map_name not in master_dict:
                master_dict[map_name] = []
            master_dict[map_name].append(new_range)
    return master_dict


def part1(input: list[str]):
    seeds = input[0].split(": ")[1].split(" ")
    master_dict: dict[str, list[tuple[int, int, int]]] = create_master_dict(input[1:])
    locations = []
    for seed in seeds:
        curr_val = int(seed)
        for lookup in LOOKUP_STEPS:
            for src, dest, delta in master_dict[lookup]:
                if curr_val >= src and curr_val < src + delta:
                    curr_val = curr_val - src + dest
                    break
        locations.append(curr_val)
    print(min(locations))


def part2(input):
    seeds = input[0].split(": ")[1].split(" ")
    seeds = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]
    master_dict: dict[str, list[tuple[int, int, int]]] = create_master_dict(input[1:])
    min_location = 1e100000000000
    total_min_seed = 1e10000000000
    for seed_range in seeds:
        for seed in range(int(seed_range[0]), int(seed_range[0]) + int(seed_range[1])):
            curr_val = int(seed)
            for lookup in LOOKUP_STEPS:
                for src, dest, delta in master_dict[lookup]:
                    if curr_val >= src and curr_val < src + delta:
                        curr_val = curr_val - src + dest
                        break
            min_location = min(min_location, curr_val)
        total_min_seed = min(total_min_seed, min_location)
    print(total_min_seed)


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
