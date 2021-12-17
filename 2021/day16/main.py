def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()[0]

def part1(input):
  print(bin(int(input, 16))[2:5])

def part2(input):
  return

def main():
  input = read_file('test.file')
  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")
  print("Running part 2...")
  part2(input)
  print("-----------------")

main()