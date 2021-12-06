def read_file(filename):
  with open(filename, 'r') as f:
    return [int(num) for num in f.read().split(",")]

def find_fish(fishes):
  total = 0
  for k,v in fishes.items():
    total = total + v
  return total

# This isn't the most memory efficient solution, but it do be runnin fast
def part1(input, num_days):
  fishes = dict.fromkeys(range(0,9), 0)
  delta_fishes = dict.fromkeys(range(0,9), 0)
  for fish in input:  # add initial values
    fishes[fish] = fishes[fish] + 1

  for day in range(1, num_days+1):
    for k,v in fishes.items():
      if v > 0 and k > 0: # for every value, store the days changes in another dict
        delta_fishes[k-1] = delta_fishes[k-1] + v
      elif k == 0 and v > 0:
        delta_fishes[6] = delta_fishes[6] + v
        delta_fishes[8] = delta_fishes[8] + v
    fishes = delta_fishes  # then at the end of the day, apply the changes
    delta_fishes = dict.fromkeys(range(0,9), 0)
  print("Number of fishes:", find_fish(fishes))

def main():
  input = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  days1 = 80
  part1(input, days1)
  print("-----------------")
  print("Running part 2...")
  days2 = 256
  part1(input, days2)
  print("-----------------")

main()