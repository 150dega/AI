# Depth First Search (DFS) using Recursion

def dfs(graph, node, visited):

    # Check if node is already visited
    if node not in visited:
        print(node, end=" ")

        # Mark node as visited
        visited.append(node)

        # Visit all neighbors
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Example Graph (Adjacency List)
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
