def read_file(filename):
  with open(filename, 'r') as f:
    return [[int(num) for num in list(line)] for line in f.read().splitlines()]

def flash(i, j, grid, flashed, num_flahses=None):
  adjs = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
  for adj in adjs:
    if i+adj[0] >= 0 and j+adj[1] >= 0 and i+adj[0] < len(grid[0]) and \
        j+adj[1] < len(grid[0]) and (i+adj[0],j+adj[1]) not in flashed:
      if grid[i+adj[0]][j+adj[1]] == 9:
        flashed.append((i+adj[0],j+adj[1]))
        grid[i+adj[0]][j+adj[1]] = 0
        flash(i+adj[0], j+adj[1], grid, flashed, num_flahses)
        if num_flahses:
          num_flahses[0] = num_flahses[0] + 1
      else:
        grid[i+adj[0]][j+adj[1]] = grid[i+adj[0]][j+adj[1]] + 1

def part1(input):
  itrs = 100
  num_flahses = [0]
  for k in range(0,itrs):
    flashed = []
    for i in range(len(input)):
      for j in range(len(input[0])):
        if (i,j) not in flashed:
          if input[i][j] == 9:
            flashed.append((i,j))
            input[i][j] = 0
            flash(i, j, input, flashed, num_flahses)
            num_flahses[0] = num_flahses[0] + 1
          else:
            input[i][j] = input[i][j] + 1
  print("Flashed:", num_flahses[0])

def part2(input):
  sync = False
  counter = 0
  while not sync:
    flashed = []
    for i in range(len(input)):
      for j in range(len(input[0])):
        if (i,j) not in flashed:
          if input[i][j] == 9:
            flashed.append((i,j))
            input[i][j] = 0
            flash(i, j, input, flashed)
          else:
            input[i][j] = input[i][j] + 1
    if len(flashed) == 100:
      sync = True
    counter = counter + 1
  print("Synced on iteration:", counter)

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