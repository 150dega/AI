goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def heuristic(state):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


def find_blank(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def solve(start):

    open_list = [start]
    visited = []

    while open_list:

        current = open_list[0]

        for state in open_list:
            if heuristic(state) < heuristic(current):
                current = state

        open_list.remove(current)
        visited.append(current)

        for row in current:
            print(row)

        print()

        if current == goal:
            print("Solved!")
            return

        x, y = find_blank(current)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:

            i, j = x + dx, y + dy

            if 0 <= i < 3 and 0 <= j < 3:

                new = [row[:] for row in current]

                new[x][y], new[i][j] = new[i][j], new[x][y]

                if new not in visited and new not in open_list:
                    open_list.append(new)


start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solve(start)
