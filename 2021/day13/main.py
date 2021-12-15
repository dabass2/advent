import numpy as np

def read_file(filename):
  with open(filename, 'r') as f:
    coords, raw_folds = f.read().split("\n\n")
    folds = []
    for fold in raw_folds.split("\n"):
      tmp = fold.split("=")
      folds.append((tmp[0][-1],int(tmp[1])))  
    return ([tuple([int(x) for x in coord.split(',')]) for coord in coords.split("\n")],folds) 

def create_paper(pts):
  pts = list(zip(*pts))
  arr = np.full((max(pts[1])+1, max(pts[0])+1), '.')
  arr[pts[1],pts[0]] = '#'
  return arr

def fold(grid, folds, once=False):
  for dir,amnt in folds:
    if dir == 'y':
      subset = np.flipud(grid)
      mask = (subset == '#')
      grid[mask] = subset[mask]
      grid = grid[0:amnt,:]
    elif dir == 'x':
      subset = np.fliplr(grid)
      mask = (subset == '#')
      grid[mask] = subset[mask]
      grid = grid[:,0:amnt]
    if once:
      break
  return grid

def part1(paper, folds):
  paper = fold(paper, folds, once=True)
  total = 0
  for row in paper:
    for elem in row:
      if elem == '#':
        total = total + 1
  print("Total number of points after one fold:", total)

def part2(paper, folds):
  paper = fold(paper, folds)
  for row in paper:
    for elem in row:
      print((" " if elem != '#' else elem), end='')
    print("")  

def main():
  input = read_file('input.file')
  coords, folds = input
  paper = create_paper(coords)
  print("-----------------")
  print("Running part 1...")
  part1(paper, folds)
  print("-----------------")
  print("Running part 2...")
  part2(paper, folds)
  print("-----------------")

main()