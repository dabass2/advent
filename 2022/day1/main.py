def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().split("\n\n")

def part1(input):
  elves = []
  for elf in input:
    total = 0
    for snack in elf.split("\n"):
      total += int(snack)
    elves.append(total)
  print(max(elves))
  part2(elves)
  return

def part2(elves):
  print("-----------------")
  print("Running part 2...")
  three_total = 0
  for _ in range(0,3):
    three_total += max(elves)
    elves.remove(max(elves))
  print(three_total)
  print("-----------------")
  return

def main():
  input = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  part1(input)

main()