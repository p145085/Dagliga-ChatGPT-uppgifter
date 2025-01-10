#4. **Bygg en slumpmässig labyrintgenerator med rekursiv backtracking.**
import random
import matplotlib.pyplot as plt

def generate_maze(width, height):
    # Skapa en grid med alla väggar
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Slumpmässigt startpunkt
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)

    # Definiera rörelser: höger, vänster, ned, upp
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(nx, ny):
        # Kolla om positionen är inom gränserna och om den är omgiven av väggar
        if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == 1:
            # Räkna angränsande celler som inte är väggar
            neighbors = 0
            for dx, dy in directions:
                if 0 <= nx + dx < height and 0 <= ny + dy < width:
                    neighbors += maze[nx + dx][ny + dy] == 0
            return neighbors <= 1
        return False

    def carve(x, y):
        # Markera nuvarande cell som en väg
        maze[x][y] = 0

        # Slumpmässig ordning på riktningarna
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                carve(nx, ny)

    carve(start_x, start_y)
    return maze

def display_maze(maze):
    # Visualisera labyrinten med matplotlib
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap="binary", interpolation="nearest")
    plt.axis("off")
    plt.show()

# Exekvera labyrintgeneratorn
width, height = 21, 21  # Måste vara udda för bästa resultat
maze = generate_maze(width, height)
display_maze(maze)
