def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def area_slack(l,w,h):
  area = ((2*l*w) + (2*w*h) + (2*h*l))
  slack = min(l*w,w*h,h*l)
  return area + slack

def part1(input):
  total = 0
  for dims in input:
    l,w,h = dims.split("x")
    total = total + area_slack(int(l),int(w),int(h))
  print("Total square feet needed:", total)

def perm_cube(l,w,h):
  cubic = l*w*h
  smallest = min((l,w),(w,h),(h,l))
  perm = (smallest[0]*2) + (smallest[1]*2)
  return cubic + perm

def part2(input):
  total = 0
  for dims in input:
    l,w,h = dims.split("x")
    total = total + perm_cube(int(l),int(w),int(h))
  print("Total square feet needed:", total)

def main():
  input = read_file('input.file')
  # print("-----------------")
  # print("Running part 1...")
  # part1(input)
  print("-----------------")
  print("Running part 2...")
  part2(input)
  print("-----------------")

main()