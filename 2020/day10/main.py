x = []
with open('test.file', 'r') as f:
  for line in f:
    value = int(line.strip())
    x.append(value)
x.sort()
print(x)

''' part 1
last = 0
totals = {1:0, 2:0, 3:1}
for i in x:
  diff = i - last
  if diff <= 3 and diff > 0:
    last = i
    totals[diff] += 1
print(totals)
'''