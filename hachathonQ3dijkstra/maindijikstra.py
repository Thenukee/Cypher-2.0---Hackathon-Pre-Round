import tkinter as tk
from collections import deque, defaultdict

def shortest_path(maze):
    # Find the start and end positions in the maze
    start = None
    end = None
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == "X":
                start = (i, j)
            elif maze[i][j] == "Y":
                end = (i, j)

    if start is None or end is None:
        return None

    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the distance dictionary with infinite distances
    distance = defaultdict(lambda: float("inf"))
    distance[start] = 0

    # Priority queue to store vertices that are being processed
    queue = [(start, 0)]
    visited = set()
    path = {}  # Define the path dictionary here

    while queue:
        # Extract the vertex with the minimum distance value
        position, dist = min(queue, key=lambda x: x[1])
        queue.remove((position, dist))

        if position == end:
            # Reconstruct the path
            current = position
            final_path = []
            while current != start:
                final_path.insert(0, current)
                current = path[current]
            return final_path

        visited.add(position)

        # Visit each edge of the current vertex
        for movement in movements:
            new_row = position[0] + movement[0]
            new_col = position[1] + movement[1]
            new_pos = (new_row, new_col)

            # Check if the new position is valid and not visited
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != 1 and new_pos not in visited:
                new_dist = dist + 1
                if new_dist < distance[new_pos]:
                    distance[new_pos] = new_dist
                    queue.append((new_pos, new_dist))
                    path[new_pos] = position  # Update the path

    return None

def draw_maze(canvas, maze, no_path=False):
    # Draw the maze on the canvas
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "X" or cell == "Y":
                color = "red"
            else:
                color = "black" if cell == 1 else "white"
            canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)
            canvas.create_text(j * 30 + 15, i * 30 + 15, text=cell, fill="black", font=("Arial", 12, "bold"))

    # Display a message if no path is found
    if no_path:
        canvas.create_text(len(maze[0]) * 30 // 2, len(maze) * 30 + 15, text="😞", fill="black", font=("Arial", 30))
        canvas.create_text(len(maze[0]) * 30 // 2, (len(maze) + 2) * 30, text="No path found!", fill="black",
                           font=("Arial", 14))

def draw_path(canvas, path, length):
    # Draw the path on the canvas
    for position in path:
        i, j = position
        canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill="yellow")
    canvas.create_text(10, (len(maze) + 1) * 30, text=f"Length: {length}", anchor="nw", font=("Arial", 14),
                       fill="black")

    # Update the color of 'X' and 'Y' cells to red
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "X" or cell == "Y":
                canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill="red")
                canvas.create_text(j * 30 + 15, i * 30 + 15, text=cell, fill="black", font=("Arial", 12, "bold"))


def shortest_path_gui(maze):
    # Create a tkinter window
    root = tk.Tk()
    root.title("Shortest Path")

    # Create a canvas to draw the maze
    canvas = tk.Canvas(root, width=len(maze[0]) * 30, height=(len(maze) + 3) * 30, bg="white")
    canvas.pack()

    # Find the shortest path in the maze
    path = shortest_path(maze)

    # Draw the maze and the path on the canvas
    if path:
        draw_maze(canvas, maze)
        draw_path(canvas, path, len(path))
    else:
        draw_maze(canvas, maze, no_path=True)

    root.mainloop()

# Test the function
maze = [
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, "X", 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, "Y", 1]
]

shortest_path_gui(maze)
