with open('input.file', 'r') as f:
  x = f.readlines()

def parseGroups(x):
  groups = []
  group = []
  # print(x)
  for i in range(len(x)+1):
    if i >= len(x):   # sad
      group = [val for sublist in group for val in sublist]
      groups.append(group)
      return groups
    if x[i] == '\n':
      group = [val for sublist in group for val in sublist]
      groups.append(group)
      group = []
    else:
      group.append(x[i].strip().split())

def checkGroup(groupDict, groupSize):
  # print(groupSize)
  total = 0
  for v in groupDict.values():
    if v == groupSize:
      total += 1
  return total

# print(parseGroups(x))
groups = parseGroups(x)
totalYes = 0
for group in groups:
  seen = []
  groupAns = {}
  for answer in group:
    # print(list(answer))
    subAns = list(answer)
    for ans in subAns:
      if ans not in seen:
        seen.append(ans)
        # totalYes += 1 # part 1
        groupAns[ans] = 1
      else:
        groupAns[ans] += 1
  totalYes += checkGroup(groupAns, len(group))
  # print(groupAns)

print(totalYes)