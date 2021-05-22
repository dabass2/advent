with open('input.file', 'r') as f:
    x = f.read().splitlines()


''' part 1 '''
# for num in x:
#   chk = 2020 - int(num)
#   if str(chk) in x:
#     print(int(num) * chk)

''' part 2 '''
for num in x:
  chk1 = 2020 - int(num)
  # print("chk1:", chk1)
  for num2 in x:
    chk2 = chk1 - int(num2)
    # print("chk2:", chk2)
    if str(chk2) in x:
      print(int(num) * int(num2) * chk2)