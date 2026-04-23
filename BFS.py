

def bfs(graph, start):
    visited = []     
    queue = []        

   
    visited.append(start)
    queue.append(start)

   
    while queue:
        node = queue.pop(0)   
        print(node, end=" ")

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call BFS function
print("BFS Traversal:")
bfs(graph, 'A')
