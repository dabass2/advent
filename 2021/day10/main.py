def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def part1(input):
  endings = {'[':']','{':'}','(':')','<':'>'}
  scores = {')':3,']':57,'}':1197,'>':25137}
  total_score = 0
  for line in input:
    chunk = list(line)
    seen_stack = []
    expected_closing = None
    for char in chunk:
      if char in endings.keys() or not expected_closing:
        seen_stack.append(char)
        expected_closing = endings[char]
      elif char == expected_closing:
        seen_stack.pop()
        if len(seen_stack) > 0:
          expected_closing = endings[seen_stack[-1]]
      else:
        total_score = total_score + scores[char]
        break
  if total_score > 0:
    print("Total score of corrupted lines:", total_score)

def part2(input):
  endings = {'[':']','{':'}','(':')','<':'>'}
  scores = {')':1,']':2,'}':3,'>':4}
  total_scores = []
  for line in input:
    chunk = list(line)
    seen_stack = []
    expected_closing = None
    for char in chunk:
      if char in endings.keys() or not expected_closing:
        seen_stack.append(char)
        expected_closing = endings[char]
      elif char == expected_closing:
        seen_stack.pop()
        if len(seen_stack) > 0:
          expected_closing = endings[seen_stack[-1]]
      else:
        seen_stack = []
        break
    if (len(seen_stack) != 0):
      score = 0
      seen_stack.reverse()
      for char in seen_stack:
        score = (score * 5) + scores[endings[char]]
      total_scores.append(score)
  total_scores.sort()
  print("Middle score of incomplete lines total:", total_scores[len(total_scores)//2])

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