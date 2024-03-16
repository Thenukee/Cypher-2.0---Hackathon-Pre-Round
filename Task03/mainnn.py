import heapq

class Node:
    def __init__(self, x, y, g_cost=float('inf'), h_cost=0, parent=None):
        self.x = x
        self.y = y
        self.g_cost = g_cost  # cost from start node to this node
        self.h_cost = h_cost  # heuristic cost (estimated cost from this node to the goal)
        self.parent = parent  # parent node

    def f_cost(self):
        return self.g_cost + self.h_cost

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def get_neighbors(grid, node):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        x, y = node.x + dx, node.y + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
            neighbors.append(Node(x, y))
    return neighbors

def reconstruct_path(current_node):
    path = []
    while current_node is not None:
        path.append((current_node.x, current_node.y))
        current_node = current_node.parent
    return path[::-1]

def astar(grid, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start[0], start[1], 0, heuristic(start_node, goal))
    heapq.heappush(open_set, (start_node.f_cost(), id(start_node), start_node))

    while open_set:
        _, _, current_node = heapq.heappop(open_set)
        if (current_node.x, current_node.y) == goal:
            return reconstruct_path(current_node)
        
        closed_set.add((current_node.x, current_node.y))
        for neighbor in get_neighbors(grid, current_node):
            if (neighbor.x, neighbor.y) in closed_set:
                continue
            tentative_g_cost = current_node.g_cost + 1
            if tentative_g_cost < neighbor.g_cost:
                neighbor.parent = current_node
                neighbor.g_cost = tentative_g_cost
                neighbor.h_cost = heuristic(neighbor, goal)
                heapq.heappush(open_set, (neighbor.f_cost(), id(neighbor), neighbor))
    
    return None

def visualize_path(grid, path):
    for x, y in path:
        if grid[x][y] != 'X' and grid[x][y] != 'Y':
            grid[x][y] = '*'

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_shortest_path_length(grid, start, goal):
    path = astar(grid, start, goal)
    if path:
        visualize_path(grid, path)
        print("Shortest path length:", len(path) - 1)
        print_grid(grid)
    else:
        print("No path found!")

# Test Case
maze = [
    ["X", 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, "Y", 1]
]
start_point = (0, 0)
end_point = (4, 3)

find_shortest_path_length(maze, start_point, end_point)
