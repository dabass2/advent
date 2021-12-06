def read_file(filename):
  with open(filename, 'r') as f:
    rtn = []
    for num in f.read().split(","):
      rtn.append(int(num))
    return rtn

def find_fish(fishes):
  total = 0
  for k,v in fishes.items():
    total = total + v
  return total

def part1(input, num_days):
  # fishes = input
  # fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
  fishes = dict([(8,0),(7,0),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0)])
  for fish in input:
    fishes[fish] = fishes[fish] + 1
  print(fishes)
  for day in range(1, num_days+1):
    print("Starting day:", day)
    for k,v in fishes.items():
      print(k,v)
      if v > 0 and k != 0:
        fishes[k] = fishes[k] - v
        fishes[k+1] = fishes[k+1] + v
      elif k == 0 and v > 0:
        fishes[0] = 0
        fishes[8] = fishes[8] + v
    print("After day:", day, fishes)
  print("Number of fishes:", find_fish(fishes))

def part2(input, num_days):
  fishes = input
  for day in range(1, num_days+1):
    # print("Starting day:", day)
    for i in range(len(fishes)):
      fish = fishes[i]
      if fish == 0:
        fishes[i] = 6
        fishes.append(8)
      else:
        fishes[i] = fish - 1
    # print("After day:", day, fishes)
  print("Number of fishes:", len(fishes))

def main():
  input = read_file('test.file')
  print("-----------------")
  print("Running part 1...")
  days1 = 2
  part1(input, days1)
  print("-----------------")
  # print("Running part 2...")
  # days2 = 256
  # part2(input, days2)
  # print("-----------------")

main()