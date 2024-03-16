def shortest_path(maze):
    start = None
    end = None
    rows = len(maze)
    cols = len(maze[0])

    # Find the start and end points
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == "X":
                start = (i, j)
            elif maze[i][j] == "Y":
                end = (i, j)

    # Check if start and end points are found
    if start is None or end is None:
        return None

    # Define the possible movements (up, down, left, right)
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Create a queue to store the positions to visit
    queue = deque([(start, 0)])

    # Create a set to store the visited positions
    visited = set([start])

    # Perform breadth-first search
    while queue:
        position, distance = queue.popleft()

        if position == end:
            return distance

        for movement in movements:
            new_row = position[0] + movement[0]
            new_col = position[1] + movement[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != 1 and (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), distance + 1))
                visited.add((new_row, new_col))

    return None

# Test the function
maze = [
    ["X", 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, "Y", 1]
]

shortest_distance = shortest_path(maze)

if shortest_distance is None:
    print("No path found!")
else:
    # Mark visited cells with a special character (e.g., '.')
    for row in range(rows):
        for col in range(cols):
            if (row, col) in visited:
                maze[row][col] = '.'

    # Mark the start and end points
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    # Print the maze with the shortest path
    for row in maze:
        print(''.join(str(cell) for cell in row))
