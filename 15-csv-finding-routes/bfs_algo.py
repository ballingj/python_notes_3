# https://favtutor.com/blogs/breadth-first-search-python
# 


graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph2 = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  print("visited: ", visited)
  print("queue: ", queue)


  while queue:
    s = queue.pop(0)
    print(s, end="\n")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        print("visited neighbours: ", visited)
        queue.append(neighbour)
        print("queue neighbours: ", queue)


# Driver Code
#bfs(visited, graph1, 'A')
bfs(visited, graph2, '5')
