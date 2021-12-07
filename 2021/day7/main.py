def read_file(filename):
  with open(filename, 'r') as f:
    return [int(num) for num in f.read().split(",")]

# nice
def the_thing_the_smart_guy_came_up_with_as_a_kid(n):
  return int((n*(n+1))/2)

# These are fast, but they work fast enough
def part1(input):
  lowest_cost = None
  for pos in range(min(input), max(input)+1):
    cost = 0
    for crab in input:
      cost = cost + abs(crab - pos)
    if lowest_cost == None or cost < lowest_cost:
      lowest_cost = cost
  print("Lowest cost move:", lowest_cost)

def part2(input):
  lowest_cost = None
  for pos in range(min(input), max(input)+1):
    cost = 0
    for crab in input:
      cost = cost + the_thing_the_smart_guy_came_up_with_as_a_kid(abs(crab-pos))
    if lowest_cost == None or cost < lowest_cost:
      lowest_cost = cost
  print("Lowest cost move:", lowest_cost)

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