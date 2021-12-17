from os import truncate


class Probe():
  def __init__(self, x_vel=0, y_vel=0):
    self.x = 0
    self.y = 0
    self.x_vel = x_vel
    self.y_vel = y_vel

  def step(self):
    self.x += self.x_vel
    self.y += self.y_vel
    self.y_vel -= 1
    if self.x_vel < 0:
      self.x_vel += 1
    elif self.x_vel > 0:
      self.x_vel -= 1

def part1(input):
  x_lim, y_lim = input
  valids = []
  highest_y = 0
  for i in range(-0,200):
    for j in range(-200,200):
      probe = Probe(i,j)
      tmp = 0
      while probe.x <= x_lim[1] and probe.y >= y_lim[0]:
        tmp = probe.y if probe.y > tmp else tmp
        if probe.x >= x_lim[0] and probe.x <= x_lim[1] and probe.y >= y_lim[0] and probe.y <= y_lim[1]:
          highest_y = tmp if tmp > highest_y else highest_y
          valids.append((i,j))
          break
        probe.step()
  print("The highest point the probe can reach is:", highest_y)
  print("The number of valid initial coords:", len(valids))

def main():
  input = [(60,94),(-171,-136)]
  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")

main()