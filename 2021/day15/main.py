import collections

def read_file(filename):
  with open(filename, 'r') as f:
    return [[int(elem) for elem in list(line)] for line in f.read().splitlines()]

def bfs(grid, start):
  queue = collections.deque([[start]])
  seen = set([start])
  goal = (len(grid[0])-1,len(grid)-1)
  print(goal)
  width = len(grid)
  height = len(grid[0])
  while queue:
    path = queue.popleft()
    x, y = path[-1]
    if (y,x) == goal:
      return path
    for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
      if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
          queue.append(path + [(x2, y2)])
          seen.add((x2, y2))

def part1(input):
  print(input)
  path = bfs(input, (0,0))
  print(path)
  total = 0
  for pt in path:
    total += input[pt[0]][pt[1]]
  print(total)

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