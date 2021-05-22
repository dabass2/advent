'''
This entire file is an affront to humanity. It should never be opened. It should never
be read. It never should've been created. The runtime of this is at least n!^n!. If anyone
ever sees this...there is no saving us.
'''

import numpy as np

f = open("input.data", "r")
wires = f.readlines()
wire1 = wires[0].split(",")
wire1[-1] = wire1[-1].rstrip()
wire2 = wires[1].split(",")
wire2[-1] = wire2[-1].rstrip()
f.close()

# print(wire1, wire2)

points = [[[0,0], 0]]
# points = {}
cmmnPts = []
steps = 0

for i in wire1:
  drtc = i[0]
  dist = int(i[1:])
  # steps += np.abs(dist)
  if drtc == "R":
    for i in range(dist):
      points.append(([points[-1][0][0]+1, points[-1][0][1]], points[-1][1]+1))
  elif drtc == "L":
    for i in range(dist,0,-1):
      points.append(([points[-1][0][0]-1, points[-1][0][1]], points[-1][1]+1))
  elif drtc == "U":
    for i in range(dist):
      points.append(([points[-1][0][0], points[-1][0][1]+1], points[-1][1]+1))
  elif drtc == "D":
    for i in range(dist,0,-1):
      points.append(([points[-1][0][0], points[-1][0][1]-1], points[-1][1]+1))

# print(points)

pts1Coords = []
pts1Steps = []
for i in points:
  pts1Coords.append(i[0])
  pts1Steps.append(i[1])

points2 = [[[0,0], 0]]
for i in wire2:
  drtc = i[0]
  dist = int(i[1:])
  # print(points2)
  if drtc == "R":
    for i in range(dist):
      points2[0] = ([points2[-1][0][0]+1, points2[-1][0][1]], points2[-1][1]+1)
      # print(points2[0])
      # if points2[0][0][0] > 0 and points2[0][0][1] > 0:
      if points2[0][0] in pts1Coords:
        cmmnPts.append(points2[0])
  elif drtc == "L":
    for i in range(dist):
      points2[0] = ([points2[-1][0][0]-1, points2[-1][0][1]], points2[-1][1]+1)
      # print(points2[0])
      # if points2[0][0][0] > 0 and points2[0][0][1] > 0:
      if points2[0][0] in pts1Coords:
        cmmnPts.append(points2[0])
  elif drtc == "U":
    for i in range(dist):
      points2[0] = ([points2[-1][0][0], points2[-1][0][1]+1], points2[-1][1]+1)
      # print(points2[0])
      # if points2[0][0][0] > 0 and points2[0][0][1] > 0:
      if points2[0][0] in pts1Coords:
        cmmnPts.append(points2[0])
  elif drtc == "D":
    for i in range(dist):
      points2[0] = ([points2[-1][0][0], points2[-1][0][1]-1], points2[-1][1]+1)
      # print(points2[0])
      # if points2[0][0][0] > 0 and points2[0][0][1] > 0:
      if points2[0][0] in pts1Coords:
        cmmnPts.append(points2[0])

# print(cmmnPts)
# print(points2)
big = np.inf
curr = None

for pt in cmmnPts:
  # print(pts1Steps[pts1Coords.index(pt[0])])
  pt1 = pts1Steps[pts1Coords.index(pt[0])]
  if pt1 + pt[1] < big:
    big = pt1 + pt[1]

# for pt in cmmnPts:
#   if pt[0] > 0 and pt[1] > 0:
#     if pt[0] + pt[1] < big:
#       big = pt[0] + pt[1]
#       curr = pt

print(big)

# big = np.inf
# currMax = [None,None]
# for point in points:
#   if point in points2:
#     # print(point)
#     tmp = point[0] + point[1]
#     if tmp < big and tmp is not 0:
#       currMax = point
#       big = tmp
#     # cmmnPts.append(point)

# print(currMax, big)
