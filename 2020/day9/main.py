x = []
with open('input.file', 'r') as f:
  for line in f:
    value = int(line.strip())
    x.append(value)

''' part 1
def containsSum(num, arr):
  for i in arr:
    val = num - i
    if val in arr:
      return True
  return False

amount = 25
lastNums = x[0:amount]
workArr = x[amount:]
for num in workArr:
  chk = containsSum(num, lastNums)
  if not chk:
    print(num)
    break
  lastNums.append(num)
  lastNums.pop(0)
'''
p1Ans = 70639851

total = 0
numArr = []
i = 0
while i <= len(x):
  i += 1
  total = sum(numArr)  # just make a running sum xD idiot
  if total < p1Ans:
    numArr.append(x[i])
  elif total > p1Ans:
    i -= 1
    tmp = numArr.pop(0)
  else:
    break

print(max(numArr) + min(numArr))
