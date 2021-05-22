lowerBound = 372037
upperBound = 905157

def dblCheck(num):
  for i in range(len(num)-1):
    if num[i] == num[i+1]:
      return True
  return False

def modDblCheck(num):
  dbl = False
  trp = False
  dblLast = None
  for i in range(len(num)-1):
    # print(num[i-1]+num[i]+num[i+1])
    # print("pre", i, dbl, trp)
    if num[i] == num[i+1] and not dbl:
      dbl = True
      dblLast = num[i]
    if i and num[i] == num[i+1] and num[i] == num[i-1]:
      trp = True
      if num[i+1] == dblLast:
        dbl = False
    else:
      trp = False
    # print("post", i, dbl, trp)
  if dbl and trp:
    return dbl
  return dbl and not trp

def lrgCheck(num):
  num = list(num)
  for i in range(len(num)-1):
    if num[i] > num[i+1]:
      return False
  return True

total = 0
print("Scanning through range: {}-{}".format(lowerBound,upperBound))
for i in range(lowerBound,upperBound):
  num = str(i)
  if modDblCheck(num) and lrgCheck(num):
    # print(num)
    total += 1 # 359 too high

print("Total Numbers: {}".format(total))

# print(modDblCheck(str(112233)), lrgCheck(str(122345)))
# print(modDblCheck(str(123456)))