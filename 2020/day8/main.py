with open('input.file', 'r') as f:
  x = f.read().split('\n')

# part 1
def part1(x):
  acc = 0
  seen = []
  i = 0
  while True:
    if i in seen:
      return acc
    seen.append(i)
    rawCmd = x[i].split(' ')
    cmd = rawCmd[0]
    val = int(rawCmd[1])
    if cmd == "acc":
      acc += val
      i += 1
    elif cmd == "jmp":
      i += val
    else:
      i += 1
    if i >= len(x):
      return acc
print(part1(x))


def modPart1(x):
  acc = 0
  seen = []
  i = 0
  while True:
    if i in seen:
      return None
    seen.append(i)
    rawCmd = x[i].split(' ')
    cmd = rawCmd[0]
    val = int(rawCmd[1])
    if cmd == "acc":
      acc += val
      i += 1
    elif cmd == "jmp":
      i += val
    else:
      i += 1
    if i >= len(x):
      return acc

for i in range(len(x)):
  rawCmd = x[i].split(' ')
  cmd,val = rawCmd
  if cmd == "nop":
    x[i] = "jmp {}".format(val)
    rtn = modPart1(x)
    if rtn:
      print(rtn)
      break
    x[i] = "nop {}".format(val)
  elif cmd == "jmp":
    x[i] = "nop {}".format(val)
    rtn = modPart1(x)
    if rtn:
      print(rtn)
      break
    x[i] = "jmp {}".format(val)