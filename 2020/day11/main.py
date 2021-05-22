with open('input.file', 'r') as f:
  x = f.readlines()

def printForest(forest):
  for line in forest:
    string = ''
    print(string.join(line))
  return

seats = []
for line in x:
  line = line.strip()
  seats.append(list(line))
newSeats = [row[:] for row in seats]

def findOcc(arr):
  num = 0
  for y in range(len(arr[0])):
    for x in range(len(arr[0])):
      if arr[y][x] == '#':
        num += 1
  return num

def checkAdj(arr, x, y):
  count = 0
  coords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for c in coords:
    try:
      # print(x,y)
      yIdx,xIdx = y+c[0],x+c[1]
      # print(yIdx, xIdx)
      if yIdx < 0 or xIdx < 0:
        continue
      if arr[yIdx][xIdx] == "#":
        count += 1
    except:
      continue
  return count

# print(checkAdj(seats, 0, 0))
# for y in range(len(seats[0])):
#   for x in range(len(seats[0])):
#     pt = seats[y][x]
#     if pt == 'L':
#       adjCount = checkAdj(seats, x, y)
#       if adjCount == 0:
#         newSeats[y][x] = '#'
#     elif pt == '#':
#       adjCount = checkAdj(seats, x, y)
#       if adjCount >= 4:
#         newSeats[y][x] = 'L'
# printForest(newSeats)
# for x in range(len(seats[0])):
#   print(newSeats[0][x], checkAdj(newSeats, x, 0))
# print(checkAdj(newSeats, 2, 0))
# seats = [row[:] for row in newSeats]
# for y in range(len(seats[0])):
#   for x in range(len(seats[0])):
#     pt = seats[y][x]
#     if pt == 'L':
#       adjCount = checkAdj(seats, x, y)
#       if adjCount == 0:
#         newSeats[y][x] = '#'
#     elif pt == '#':
#       adjCount = checkAdj(seats, x, y)
#       if adjCount >= 4:
#         newSeats[y][x] = 'L'
# printForest(newSeats)
# print(checkAdj(newSeats, 0, 0))

while True:
  # printForest(seats)
  # print('\n')
  for y in range(len(seats[0])):
    for x in range(len(seats[0])):
      if seats[y][x] == 'L':
        adjCount = checkAdj(seats, x, y)
        if not adjCount:
          newSeats[y][x] = '#'
      elif seats[y][x] == '#':
        adjCount = checkAdj(seats, x, y)
        # print(y, x, adjCount)
        if adjCount >= 4:
          newSeats[y][x] = 'L'
  if newSeats == seats:
    print(findOcc(newSeats))
    break
  seats = [row[:] for row in newSeats]

# print(forest)
# printForest(seats)
# print('\n')
# printForest(newForest)