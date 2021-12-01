def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def part1(depths):
  last = None
  inc_count = 0
  for depth in depths:
    if last and int(depth) > last:
      inc_count = inc_count + 1
    last = int(depth)
  print("Num incs", inc_count)

def part2(depths):
  last = None
  inc_count = 0

  group1 = []
  group2 = []
  group3 = []

  i = 0
  n = len(depths)
  while (i <= n):
    if i == n:
      if sum(group1) > last or sum(group2) > last or sum(group3) > last:
        inc_count = inc_count + 1
      break

    val = int(depths[i])

    len1 = len(group1)
    if len1 < 3:
      group1.append(val)
    elif len1 == 3:
      if last and sum(group1) > last:
        inc_count = inc_count + 1
      last = sum(group1)
      group1 = []
      group1.append(val)

    len2 = len(group2)
    if len2 < 3 and i > 0:
      group2.append(val)
    elif len2 == 3:
      if last and sum(group2) > last:
        inc_count = inc_count + 1
      last = sum(group2)
      group2 = []
      group2.append(val)

    len3 = len(group3)
    if len3 < 3 and i > 1:
      group3.append(val)
    elif len3 == 3:
      if last and sum(group3) > last:
        inc_count = inc_count + 1
      last = sum(group3)
      group3 = []
      group3.append(val)
    i = i + 1
  print("Num incs", inc_count)

def main():
  input = read_file("input.file")
  print("Running part 1...")
  part1(input)

  print("Running part 2...")
  part2(input)

main()