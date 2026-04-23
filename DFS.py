

def dfs(graph, node, visited):


    if node not in visited:
        print(node, end=" ")


        visited.append(node)

        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# List to store visited nodes
visited = []

# Call DFS function
print("DFS Traversal:")
dfs(graph, 'A', visited)
