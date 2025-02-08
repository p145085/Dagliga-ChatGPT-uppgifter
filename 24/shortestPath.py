#24. **Skapa en funktion som returnerar längden på den kortaste vägen i en labyrint.**
from collections import deque

def shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Upp, ner, vänster, höger
    queue = deque([(start[0], start[1], 0)])  # (x, y, steg)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        # Om vi har nått målet, returnera stegen
        if (x, y) == end:
            return steps

        # Utforska alla möjliga rörelser
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # Om ingen väg hittas

# Exempel på labyrint (0 = väg, 1 = vägg)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Startpunkt (rad, kolumn)
end = (4, 4)    # Målpunkt (rad, kolumn)

result = shortest_path(maze, start, end)
print("Längden på den kortaste vägen:", result)
