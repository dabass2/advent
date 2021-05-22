arr = []
with open('test.file', 'r') as f:
  for line in f:
    arr.append(line.strip())

print(arr)

direction = 0
x,y = 0,0
for cmd in arr:
  action = cmd[0]
  value = int(cmd[1:])
  if action == "N":
    y += value
  elif action == "S":
    y -= value
  elif action == "E":
    y += value
  elif action == "W":
    y -= value
  elif action == "R":
    direction -= value
  elif action == "L":
    direction += value
  if abs(direction) == 360:
    direction = 0
  print(x,y,direction)

print(abs(x) + abs(y))
