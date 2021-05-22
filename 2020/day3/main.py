with open('input.file', 'r') as f:
  x = f.readlines()

def printForest(forest):
  for line in forest:
    string = ''
    print(string.join(line))
  return

forest = []
for line in x:
  line = line.strip()
  forest.append(list(line))

def findTrees(slope):
  x,y = 0,0
  treeCount = 0
  while (y < len(forest)):
    if forest[y][x] == '#':
      treeCount += 1
    x += slope[0]
    y += slope[1]
    if x >= len(forest[0]):
      x = x - len(forest[0])
  return treeCount

# slopes = [(3,1)] # part 1
slopes  = [(1,1),(3,1),(5,1),(7,1),(1,2)]  # part 2

treeMul = 1
for slope in slopes:
  treeMul *= findTrees(slope)

print(treeMul)
# printForest(forest)
