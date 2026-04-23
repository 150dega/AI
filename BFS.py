# Breadth First Search (BFS) using Queue

def bfs(graph, start):
    visited = []      # List to keep track of visited nodes
    queue = []        # Queue for BFS traversal

    # Add starting node
    visited.append(start)
    queue.append(start)

    # Traverse the graph
    while queue:
        node = queue.pop(0)   # Remove first element (FIFO)
        print(node, end=" ")

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# Example Graph (Adjacency List)
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
