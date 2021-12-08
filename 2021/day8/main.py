def read_file(filename):
  with open(filename, 'r') as f:
    return [(line.split("|")[0].rstrip().split(" "),line.split("|")[1].lstrip().split(" ")) for line in f.read().splitlines()]

def part1(input):
  counter = 0
  valids = [2,3,4,7]
  for patterns, output in input:
    for digits in output:
      if len(digits) in valids:
        counter = counter + 1
  print(counter)

def find_easy(patterns, cipher):
  lookup = {7:8,2:1,4:4,3:7}
  for pattern in patterns:
    if len(pattern) in lookup.keys():
      cipher[lookup[len(pattern)]] = set(list(pattern))

def fill_cipher(patterns, cipher):
  find_easy(patterns, cipher) # fill cipher with 1,4,7,8 and remove those patterns
  for pattern in patterns:
    tmp_set = set(list(pattern))
    if len(tmp_set & cipher[1]) == 2:
      if not cipher[3] and len(tmp_set ^ cipher[8]) == 2 and len(tmp_set) == 5:
        cipher[3] = tmp_set
      elif not cipher[9] and len((tmp_set ^ cipher[8]) & cipher[4]) == 0 and len(tmp_set) == 6:
        cipher[9] = tmp_set
      else: # I don't know if this always works...
        cipher[0] = tmp_set
    else:
      if not cipher[6] and len(tmp_set ^ cipher[8]) == 1 and len(tmp_set) == 6:
        cipher[6] = tmp_set
      elif not cipher[2] and len((tmp_set ^ cipher[8]) ^ cipher[4]) == 2 and len(tmp_set) == 5:
        cipher[2] = tmp_set
      else: # I don't know if this always works...
        cipher[5] = tmp_set

def part2(input):
  total = 0
  for patterns, outputs in input:
    cipher = dict.fromkeys(range(0,10),'')
    fill_cipher(patterns, cipher)
    entry = ''
    for output in outputs:
      for k,v in cipher.items():
        if len(v ^ set(list(output))) == 0:
          entry = entry + str(k)
    total = total + int(entry)
  print(total)

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