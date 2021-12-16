from collections import Counter

def read_file(filename):
  with open(filename, 'r') as f:
    base, steps = f.read().split("\n\n")
    steps_dict = {}
    for step in steps.split("\n"):
      pair, elem = step.split("->")
      steps_dict[pair.rstrip()] = elem.lstrip()
    base_dict = Counter()
    for i in range(len(base)-1):
      base_dict[base[i:i+2]] += 1
    return (base_dict,steps_dict)

def count_total(polymer):
  totals = Counter()
  for k,v in polymer.items():
    totals[k[1]] += v
  totals["S"] += 1
  return totals

def part1(input, steps):
  poly_store, insert_rules = input
  for _ in range(steps):
    for key,val in list(filter(lambda x: x[1] > 0, list(poly_store.items()))):
      if key[:2] not in insert_rules.keys():
        continue
      insertee = insert_rules[key[:2]]
      poly_store[key] -= val
      poly_store[key[0]+insertee] += val
      poly_store[insertee+key[1]] += val
  counts = count_total(poly_store)
  print(max(counts.values()) - min(counts.values()))

def main():
  input = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  part1(input, steps=10)
  print("-----------------")
  print("Running part 2...")
  part1(input, steps=40)
  print("-----------------")

main()