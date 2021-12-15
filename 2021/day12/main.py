from os import path


def read_file(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines()

def create_caves(input):
  graph = {"start":[]}
  for path in input:
    nodes = path.split("-")
    if nodes[0] not in graph.keys():
      graph[nodes[0]] = []
    if nodes[1] not in graph.keys():
      graph[nodes[1]] = []
    graph[nodes[0]].append(nodes[1])
    graph[nodes[1]].append(nodes[0])
  graph["end"] = []
  return graph

def has_small(path):
  for node in path:
    if node.islower():
      return True
  return False

def main():
  input = read_file('input.file')

main()