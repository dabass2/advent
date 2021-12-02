def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def part1(commands):
  x, y = 0, 0

  for command in commands:
    direction, intensity = command.split(" ")
    intensity = int(intensity)

    if direction == "forward":
      x = x + intensity
    elif direction == "down":
      y = y + intensity
    elif direction == "up":
      y = y - intensity
    else:
      print("invalid direction homie")

  print("Final horz. pos:", x)
  print("Final depth:", y)
  print("Product of the two:", x*y)

def part2(commands):
  x, y, aim = 0, 0, 0

  for command in commands:
    direction, intensity = command.split(" ")
    intensity = int(intensity)

    if direction == "forward":
      x = x + intensity
      y = y + (aim*intensity)
    elif direction == "down":
      aim = aim + intensity
    elif direction == "up":
      aim = aim - intensity
    else:
      print("invalid direction homie")

  print("Final horz. pos:", x)
  print("Final depth:", y)
  print("Product of the two:", x*y)

def main():
  input = read_file('input.file')

  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")
  print("Running part 2...")
  part2(input)
  print("-----------------")

main()