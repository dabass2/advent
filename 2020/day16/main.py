from typing import Tuple


with open('input.file', 'r') as f:
  x = f.readlines()

allBounds = []

i = 0
while True:
    # print(x[i].rstrip(), i)
    if (x[i] == "\n"):
        i += 1
        continue

    if (x[i].rstrip() == "your ticket:"):
        break

    bounds = x[i].rstrip().split()
    upper = bounds[-1].split("-")
    lower = bounds[-3].split("-")

    lower = [ int(x) for x in lower]
    upper = [ int(x) for x in upper]

    allBounds.append(lower)
    allBounds.append(upper)
    
    i += 1

# print(allBounds)

i += 1
usrTicket = x[i].rstrip().split(",")
usrTicket = [ int(x) for x in usrTicket ]
# print(usrTicket)
i += 3

allTickets = []

while i < len(x):
    tix = x[i].rstrip().split(",")
    tix = [ int(x) for x in tix ]

    allTickets.append(tix)
    i += 1

# print(allTickets)

def checkValid(num):
    for bound in allBounds:
        if num >= bound[0] and num <= bound[1]:
            return True
    return False

valid = []
invalid = []
for ticket in allTickets:
    validTic = 1
    wrongNum = None
    # print(ticket)
    for num in ticket:
        # print(num)
        if not checkValid(num):
            validTic = 0
            wrongNum = num
            break
    if validTic:
        valid.append(ticket)
    else:
        invalid.append(wrongNum)

# print(valid)
# print(invalid)

print(sum(invalid))

# bounds = x[0].rstrip().split()
# upper = bounds[-1].split("-")
# lower = bounds[-3].split("-")

# lower = [ int(x) for x in lower]
# upper = [ int(x) for x in upper]

# allBounds.append(lower)
# allBounds.append(upper)

# # checking fn
# for i in range(10):
#     for bound in allBounds:
#         if i >= bound[0] and i <= bound[1]:
#             print(i)
