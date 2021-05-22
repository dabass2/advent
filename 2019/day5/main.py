import csv

intCode = None
with open('test.data') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    intCode = row

intCode = list(map(int, intCode))

'''
Parses the opcode from the instruction given. Returns a tuple

param3 mode, param2 mode, param1 mode, opcode

'''
def opParser(rawCode):
  rawCode = str(rawCode)    # me dum
  # step = 5-len(rawCode)
  rawCode = '0'*(5-len(rawCode)) + rawCode   # add back in any leading zeros
  # print(rawCode)
  return (int(rawCode[0]), int(rawCode[1]), int(rawCode[2]), int(rawCode[3:]))

i = 0
steps = {1:4,2:4,3:2,4:2}
while i < len(intCode):
  # print(i)
  try:
    mode3, mode2, mode1, cmd = opParser(intCode[i])
    step = steps[cmd]
    param1 = intCode[i+1] if mode1 else intCode[intCode[i+1]]
    param2 = intCode[i+2] if mode2 else intCode[intCode[i+2]]
    param3 = intCode[intCode[i+3]] if mode3 else intCode[i+3]
    # print(mode3, mode2, mode1, cmd)
    # print(param1, param2, param3, step)
    if cmd == 1:
      newNum = param1 + param2
      intCode[param3] = newNum
    elif cmd == 2:
      newNum = param1 * param2
      intCode[param3] = newNum
    elif cmd == 3:
      inpt = int(input("input:"))
      intCode[param1] = inpt
    elif cmd == 4:
      print(param1)
    elif cmd == 99:
      break
  except Exception as e:
    break
  # print(intCode)
  i = i + step

print(intCode)