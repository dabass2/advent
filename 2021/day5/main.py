def read_file(filename):
  with open(filename, 'r') as f:
    input = f.read().splitlines()
    vals = []
    max_x, max_y = 0, 0
    for val in input:
      pair = []
      for pt in val.split("->"):
        pt = pt.split(",")
        x, y = int(pt[0]), int(pt[1])
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        pair.append((x,y))
      vals.append(pair)
    return (vals, (max_x, max_y))

def print_grid(grid):
  for row in grid:
    print(row)

def find_score(grid):
  score = 0
  for row in grid:
    for col in row:
      if col >= 2:
        score = score + 1
  return score

def part1(input):
  pts = input[0]
  grid = [[0 for x in range(input[1][0]+1)] for y in range(input[1][1]+1)]
  for pair_one, pair_two in pts:
    if pair_one[0] == pair_two[0]:
      y = pair_one[0]
      min_itr = min(pair_one[1], pair_two[1])
      max_itr = max(pair_one[1], pair_two[1])
      for i in range(min_itr, max_itr+1):
        grid[i][y] = grid[i][y] + 1
    elif pair_one[1] == pair_two[1]:  # idk if this will cause an issue, but it hasn't yet
      x = pair_one[1]
      min_itr = min(pair_one[0], pair_two[0])
      max_itr = max(pair_one[0], pair_two[0])
      for i in range(min_itr, max_itr+1):
        grid[x][i] = grid[x][i] + 1
  print("Number of overlaps:", find_score(grid))
  return

def part2(input):
  pts = input[0]
  grid = [[0 for x in range(input[1][0]+1)] for y in range(input[1][1]+1)]
  for pair_one, pair_two in pts:
    if pair_one[0] == pair_two[0]:
      y = pair_one[0]
      min_itr = min(pair_one[1], pair_two[1])
      max_itr = max(pair_one[1], pair_two[1])
      for i in range(min_itr, max_itr+1):
        grid[i][y] = grid[i][y] + 1
    elif pair_one[1] == pair_two[1]:  # idk if this will cause an issue, but it hasn't yet
      x = pair_one[1]
      min_itr = min(pair_one[0], pair_two[0])
      max_itr = max(pair_one[0], pair_two[0])
      for i in range(min_itr, max_itr+1):
        grid[x][i] = grid[x][i] + 1
    else: # order the points to smallest = start and largest = end, then determine slope of line, finally draw the points
      start = min(pair_one, pair_two)
      end = max(pair_one, pair_two)
      slope = 1 if start[1] < end[1] else -1  # p1[1] == p2[1] won't happen here
      j = start[1]
      for i in range(start[0], end[0]+1):
        grid[j][i] = grid[j][i] + 1
        j = j + slope
  print("Number of overlaps:", find_score(grid))
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