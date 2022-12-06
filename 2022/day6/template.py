def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()[0]

def solve(input, str_len=4):
  seq = input[:str_len]
  for i, c in enumerate(list(input)):
    if len(set(seq)) < str_len:
      seq = seq[1:] + c
    else:
      print(i)
      break
  return

def main():
  input = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  solve(input)
  print("-----------------")
  print("Running part 2...")
  solve(input, 14)
  print("-----------------")

main()