def read_file(filename):
  with open(filename, 'r') as f:
    text = f.read()
    boxes, cmds = text.split("\n\n")
    cmds = cmds.split("\n")
    cmds = [list(cmd.replace("move", "").replace("from", "").replace("to", "").lstrip().replace("  ", "")) for cmd in cmds]
    layout = [[] for _ in range(9)]
    for box in boxes.split('\n')[:-1]:
      for i, idx in enumerate(range(1,45,4)):
        if idx < len(box) and box[idx].isalpha():
          layout[i].append(box[idx])
    [l.reverse() for l in layout]
    return cmds, layout

def part1(cmds, layout):
  for cmd in cmds:
    raw_cmd = list(cmd)
    if len(raw_cmd) == 4:
      c = raw_cmd.pop(1)
      raw_cmd[0] += c
    cmd = raw_cmd
    amnt, src, dest = list(cmd)
    change = layout[int(src)-1][-1*int(amnt):]
    change.reverse()
    layout[int(dest)-1].extend(change)
    del layout[int(src)-1][-1*int(amnt):]
  for l in layout:
    if l:
      print(l[-1], end="")
  print("")
  return

def part2(cmds, layout):
  for cmd in cmds:
    raw_cmd = list(cmd)
    if len(raw_cmd) == 4:
      c = raw_cmd.pop(1)
      raw_cmd[0] += c
    cmd = raw_cmd
    amnt, src, dest = list(cmd)
    layout[int(dest)-1].extend(layout[int(src)-1][-1*int(amnt):])
    del layout[int(src)-1][-1*int(amnt):]
  for l in layout:
    if l:
      print(l[-1], end="")
  print("")
  return

def main():
  cmds, layout = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  part1(cmds, layout)
  print("-----------------")
  print("Running part 2...")
  part2(cmds, layout)
  print("-----------------")

main()