def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def part1(input):
  # Should probably work with the numbers in raw binary, but...
  times_seen = [0] * len(input[0])
  for num in input:
    for i in range(len(num)):
      if num[i] == '1':
        times_seen[i] = times_seen[i] + 1

  gamma = ''
  epsilon = ''
  for seen_rate in times_seen:
    if seen_rate > len(input)/2: # what if rate == len/2 ? doesn't matter I guess lole
      gamma = gamma + '1'
      epsilon = epsilon + '0'
    else:
      gamma = gamma + '0'
      epsilon = epsilon + '1'
  print("Gamma: {} | Epsilon: {} | Pwr Consm: {}".format(int(gamma, 2), int(epsilon, 2), int(gamma, 2)*int(epsilon, 2)))

# I'm p sure these can be combined, but I got lazy
def find_oxy(input):  # not the felony
  ones = []
  zeros = []
  oxy_gen = input
  curr_bit = 0
  while len(oxy_gen) > 1:
    for num in oxy_gen:
      if num[curr_bit] == '1':
        ones.append(num)
      else:
        zeros.append(num)
    if len(ones) >= len(zeros):
      oxy_gen = ones
    else:
      oxy_gen = zeros
    ones = []
    zeros = []
    curr_bit = curr_bit + 1
  return int(oxy_gen[0],2)

def find_c02(input):
  ones = []
  zeros = []
  c02_scrub = input
  curr_bit = 0
  while len(c02_scrub) > 1:
    for num in c02_scrub:
      if num[curr_bit] == '1':
        ones.append(num)
      else:
        zeros.append(num)
    if len(ones) < len(zeros):
      c02_scrub = ones
    else:
      c02_scrub = zeros
    ones = []
    zeros = []
    curr_bit = curr_bit + 1
  return int(c02_scrub[0],2)

def part2(input):
  oxy = find_oxy(input)
  c02 = find_c02(input)
  print("Oxygen rating: {} | C02 Rating: {} | Life Support Rating: {}".format(oxy, c02, oxy*c02))

def main():
  input = read_file('test.file')
  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")
  print("Running part 2...")
  part2(input)
  print("-----------------")

main()