from math import floor,ceil

with open('input.file', 'r') as f:
  x = f.readlines()

# binary search knows where you sleep
def findRow(rowCode):
  minRow, maxRow = 0,127
  final = 0
  for char in rowCode:
    if char == "F":
      maxRow = floor((maxRow + minRow) / 2)
      final = minRow
    elif char == "B":
      minRow = ceil((maxRow + minRow) / 2)
      final = maxRow
  return final

def findCol(colCode):
  minCol, maxCol = 0,7
  final = 0
  for char in colCode:
    if char == "L":
      maxCol = floor((maxCol + minCol) / 2)
      final = minCol
    elif char == "R":
      minCol = ceil((maxCol + minCol) / 2)
      final = maxCol
  return final

# biggest = 0
seatIDS = []
for code in x:
  code = code.strip()
  rowCode,colCode = code[:-3],code[-3:]
  row = findRow(rowCode)
  col = findCol(colCode)
  seatID = (row * 8) + col
  seatIDS.append(seatID)
  # if seatID > biggest:  # part 1
  #   biggest = seatID

seatIDS.sort()
b = [x for x in range(seatIDS[0], seatIDS[-1] + 1)] # part 2
seatIDS = set(seatIDS)
print (list(seatIDS ^ set(b)))