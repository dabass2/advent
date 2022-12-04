def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def part1(input):
  rpt_pairs = 0
  for grp in input:
    elf1, elf2 = grp.split(",")
    e1l, e1r = elf1.split("-")
    e2l, e2r = elf2.split("-")
    # inc count if
    # elf1 has a lower bound less than elf2's lower bound and elf1's
    # upper bound is greater than elf2's upper bound (elf1 does all of elf2's work)
    # or
    # elf1's lower bound is greater than elf2's lower bound and elf1's upper bound is
    # less than elf2's upper bound (elf2 does all the work elf1 just did)
    if int(e1l) <= int(e2l) and int(e1r) >= int(e2r) or \
       int(e1l) >= int(e2l) and int(e1r) <= int(e2r):
      rpt_pairs += 1
  print(rpt_pairs)
  return

def part2(input):
  ovr_count = 0
  for grp in input:
    elf1, elf2 = grp.split(",")
    e1l, e1r = elf1.split("-")
    e2l, e2r = elf2.split("-")
    # if elf1's lower bound is less than elf2's upper bound and elf1's upper bound
    # is less than elf2's lower bound then they will intersect at least once, so inc count
    if int(e1l) <= int(e2r) and int(e1r) >= int(e2l):
      ovr_count += 1
  print(ovr_count)
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