with open('input.file', 'r') as f:
  x = f.readlines()

def createGraph(x):
  G = {}
  for line in x:
    rawLine = line.strip().split('bags contain')
    vertex = rawLine[0].strip()
    rawInsides = rawLine[1].split(',')
    edges = []
    for i in rawInsides:
      if i == ' no other bags.':
        # edges = [None]
        break
      insides = i.strip().split(' ')
      num = int(insides[0])
      bag = (str(insides[1] + ' ' + insides[2]), num)
      edges.append(bag)
    G[vertex] = edges
  return G

''' part 1
def traverse(V, G):
  count = 0
  target = "shiny gold"
  seen = []
  queue = []
  queue.append(V)
  while queue:
    # print(queue)
    v = queue.pop(0)
    # print(v)
    for edge in G[v]:
      if edge not in seen:
        queue.append(edge)
        seen.append(edge)
        if edge == target:
          count += 1
  return count
'''

G = createGraph(x)
target = 'shiny gold'

''' part 1
seen = []
connected = []
total = 0
for vert in G.keys():
  total += traverse(vert, G) 
'''

# doesn't work idk why 
def traverse2(V, G, costs):
  # print(V[0])
  vert, numBags = V
  print(vert, numBags)
  cost = 0
  if not G[vert]:
    return 1
  for edge in G[vert]:
    edgeVert, edgeWgt = edge
    try:
      cost += edgeWgt * costs[edgeVert]
    except:
      costs[edgeVert] = traverse2(edge, G, costs)
      if G[edgeVert]:
        cost += (edgeWgt * costs[edgeVert]) + edgeWgt
      else:
        cost += edgeWgt * costs[edgeVert]
  # costs[vert] = cost
  return cost

costs = {}
total = 0
queue = G[target]
# print(G)
test = ("shiny gold", 1)
print(traverse2(test, G, costs))
print(costs)