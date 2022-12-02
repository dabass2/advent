def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

PLAY_SCORES = {
  "X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3
}
LOST_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6
COUNTERS = {
  "A": "Y", "B": "Z", "C": "X"
}
LOSERS = {
  "A": "C", "B": "A", "C": "B"
}
MAPPING = {
  "A": "X", "B": "Y", "C": "Z"
}

def score_round(opp: str, play: str) -> int:
  base_score: int = PLAY_SCORES[play]
  if play == MAPPING[opp] or play == opp:
    return base_score + DRAW_SCORE
  elif play in COUNTERS[opp]:
    return base_score + WIN_SCORE
  return base_score + LOST_SCORE

def part1(input: list) -> None:
  total: int = 0
  for round in input:
    opp, play = round.split(" ")
    total += score_round(opp, play)
  print(total)
  return

def part2(input: list) -> None:
  total: int = 0
  for round in input:
    opp, outcome = round.split(" ")
    play: str = ""
    if outcome == "X":
      play = LOSERS[opp]
    elif outcome == "Y":
      play = opp
    else:
      play = COUNTERS[opp]
    total += score_round(opp, play)
  print(total)
  return

def main() -> None:
  input = read_file('input.file')
  print("-----------------")
  print("Running part 1...")
  part1(input)
  print("-----------------")
  print("Running part 2...")
  part2(input)
  print("-----------------")

main()