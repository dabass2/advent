with open('input.file', 'r') as f:
    x = f.read().splitlines()

def parseSegment(segment):
  raw = segment.split()
  rawNums = raw[0].split('-')
  rawChr = raw[1].split(':')[0]
  rawStr = raw[2]
  return ((int(rawNums[0]),int(rawNums[1])), rawChr, rawStr)

''' part 1 '''
# total = 0
# for segment in x:
#   bounds, char, string = parseSegment(segment)
#   count = string.count(char)
#   if count >= bounds[0] and count <= bounds[1]:
#     total += 1

''' part 2 '''
total = 0
for segment in x:
  indxs, char, string = parseSegment(segment)
  if string[indxs[0]-1] == char and string[indxs[1]-1] == char:
    continue
  elif string[indxs[0]-1] == char or string[indxs[1]-1] == char:
    total += 1 

print(total)