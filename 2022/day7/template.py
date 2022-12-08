def read_file(filename):
    fs = {"/": {
      "..": None,
      "dirs": [],
      "files": [],
      "size": 0
    }}
    curr_fold_name = "/"
    curr_fold = fs[curr_fold_name]
    add_to_folder = False
    with open(filename, "r") as f:
      lines = f.read().splitlines()
      for line in lines:
        vals = line.split(" ")
        if vals[0] == "$" and vals[1] == "cd":
          curr_fold_name = curr_fold[".."] if vals[2] == ".." else vals[2]
          curr_fold = fs[curr_fold_name]
        elif vals[0] == "$" and vals[1] == "ls":
          add_to_folder = True
        elif add_to_folder and vals[0] == "dir":
          fs[vals[1]] = {"..": curr_fold_name, "dirs": [], "files": [], "size": 0}
          curr_fold["dirs"].append(vals[1])
        elif add_to_folder and vals[0].isnumeric():
          file_size, file_name = vals
          curr_fold["files"].append((file_name, int(file_size)))
          curr_fold["size"] += int(file_size)
    calc_sizes(fs)
    return fs

def calc_sizes(fs):
  for _, dir_info in fs.items():
    dirs = dir_info["dirs"]
    while len(dirs) > 0:
      dir = fs[dirs.pop(0)]
      dirs[0:0] = dir["dirs"]
      dir_info["size"] += dir["size"]

def part1(input):
    total = 0
    for _, dir_info in input.items():
      if dir_info["size"] <= 100000:
        total += dir_info["size"]
    print(total)
    return

def part2(input):
    return

def main():
    input = read_file("input.file")
    print("-----------------")
    print("Running part 1...")
    part1(input)
    print("-----------------")
    # print("Running part 2...")
    # part2(input)
    # print("-----------------")


main()
