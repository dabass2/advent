class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def read_file(filename):
  with open(filename, 'r') as f:
    return [list(l) for l in f.read().splitlines()]

def print_trees(trees):
  for row in trees:
    for tree in row:
      if not tree:
        print(f"{bcolors.FAIL}{tree}{bcolors.ENDC}", end="\t", flush=True)
      else:
        print(f"{bcolors.OKGREEN}{tree}{bcolors.ENDC}", end="\t", flush=True)
    print("")

def find_hidden(tree_mask):
  total = 0
  for row in tree_mask:
    for tree in row:
      if tree:
        total += 1
  print(total)

def part1(input):
  bit_mask = [[False for _ in range(len(input[0]))] for _ in range(len(input))]
  for i in range(len(input)):
    for j in range(len(input[0])):
      print(input[j][i])
      
    break
    # for j in range(len(input[0])):
    #   print(input[i][j])
  # print_trees(bit_mask)
  # find_hidden(bit_mask)
  return

def part2(input):
  return

def main():
  input = read_file('test.file')
  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")
  # print("Running part 2...")
  # part2(input)
  # print("-----------------")

main()