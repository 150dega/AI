def a_star(graph, heuristic, start, goal):

    open_list = [start]
    closed_list = []

    g = {start: 0}
    parent = {start: None}

    while open_list:

        current = open_list[0]

        for node in open_list:
            if g[node] + heuristic[node] < g[current] + heuristic[current]:
                current = node

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        open_list.remove(current)
        closed_list.append(current)

        for neighbor, cost in graph[current]:

            if neighbor in closed_list:
                continue

            new_cost = g[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)

            elif new_cost >= g.get(neighbor, float('inf')):
                continue

            g[neighbor] = new_cost
            parent[neighbor] = current

    return None


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 0
}

path = a_star(graph, heuristic, 'A', 'F')

print("Optimal Path:", path)
