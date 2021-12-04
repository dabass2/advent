# Ya'll like for loops? 👀
def read_file(filename):
  with open(filename, 'r') as f:
    input = f.read().splitlines()
    rand_nums = [int(x) for x in input[0].split(",")]
    boards = []
    curr_idx = 0
    curr_board = []
    for row in input[2:]:
      board_row = row.split(" ")
      if len(board_row) == 1 or row == input[-1]:
        curr_idx = curr_idx + 1
        if row == input[-1]:
          curr_board.append([int(x) for x in board_row if x])
        boards.append(curr_board)
        curr_board = []
      else:
        curr_board.append([int(x) for x in board_row if x])
    return (rand_nums, boards)

def get_score(board):
  sum = 0
  for i in range(5):
    for j in range(5):
      if (board[i][j]):
        sum = sum + board[i][j]
  return sum

def find_win(board, x, y):
  for i in range(5):  # check rows
    if (board[x][i]):
      break
    if (i == 4):
      return get_score(board)

  for i in range(5):  # check cols
    if (board[i][y]):
      break
    if (i == 4):
      return get_score(board)
  return False

def find_board_num(board, num):
  for i in range(5):
    for j in range(5):
      if board[i][j] == num:
        board[i][j] = None
        return find_win(board, i, j)

def part1(nums, boards):
  for num in nums:
    for board in boards:
      result = find_board_num(board, num)
      if result:
        print("First winning board score:", result * num)
        return

def part2(nums, boards):
  finished_boards = []
  last_win = None # I didn't use this to get the answer, but it's nice for printing
  for num in nums:
    for board in boards:
      idx = boards.index(board)
      if idx not in finished_boards:
        result = find_board_num(board, num)
        if result:
          finished_boards.append(idx) # once the board has won, add it to the ignore list
          last_win = result * num
          if len(finished_boards) == len(boards):
            print("Last winning board score:", last_win)
            return

def main():
  nums, boards = read_file('input.file')

  print("-----------------")
  print("Running part 1...")
  part1(nums, boards)
  print("-----------------")
  print("Running part 2...")
  part2(nums, boards)
  print("-----------------")

main()