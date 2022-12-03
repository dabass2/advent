from collections import Counter

def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def get_priority(char):
  letters = list("abcdefghijklmnopqrstuvwxyz")
  return letters.index(char.lower()) + (26 if char.isupper() else 0) + 1

def part1(input):
  total = 0
  for sack in input:
    comp1, comp2 = sack[:len(sack)//2], sack[len(sack)//2:]
    chars1, chars2 = Counter(comp1), Counter(comp2)
    for char in chars1:
      if char in chars2.keys():
        total += get_priority(char)
  print(total)
  return

def part2(input):
  total = 0
  for i in range(0, len(input), 3):
    bag1, bag2, bag3 = input[i:i+3]
    chars1, chars2, chars3 = Counter(bag1), Counter(bag2), Counter(bag3)
    for char in chars1:
      if char in chars2.keys() and char in chars3.keys():
        total += get_priority(char)
  print(total)
  return

def main():
  input = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")
  print("Running part 2...")
  part2(input)
  print("-----------------")

main()