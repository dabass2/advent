def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

moves = {'(':1,')':-1}
pos = 0
neg = None
input = read_file("input.file")[0]
for i in range(len(input)):
  pos = pos + moves[input[i]]
  if not neg and pos < 0:
    neg = i+1

print("Final floor:", pos)
print("First negative floor:", neg)