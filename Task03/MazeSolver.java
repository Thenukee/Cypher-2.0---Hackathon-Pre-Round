import java.util.*;

public class MazeSolver {

    static class Point {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int bfs(char[][] maze, Point start, Point end) {
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        int n = maze.length;
        int m = maze[0].length;

        boolean[][] visited = new boolean[n][m];
        Queue<Point> queue = new LinkedList<>();
        queue.offer(start);
        visited[start.x][start.y] = true;
        int steps = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Point current = queue.poll();
                if (current.x == end.x && current.y == end.y)
                    return steps;

                for (int j = 0; j < 4; j++) {
                    int nx = current.x + dx[j];
                    int ny = current.y + dy[j];

                    if (nx >= 0 && nx < n && ny >= 0 && ny < m && maze[nx][ny] != '1' && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.offer(new Point(nx, ny));
                    }
                }
            }
            steps++;
        }
        return -1; // No path found
    }

    public static void main(String[] args) {
        char[][] maze = {
                {'X', '0', '1', '0', '0'},
                {'0', '1', '0', '1', '0'},
                {'0', '0', '0', '0', '1'},
                {'0', '1', '0', '1', '0'},
                {'0', '0', '0', 'Y', '1'}
        };

        Point start = null, end = null;
        for (int i = 0; i < maze.length; i++) {
            for (int j = 0; j < maze[0].length; j++) {
                if (maze[i][j] == 'X') {
                    start = new Point(i, j);
                } else if (maze[i][j] == 'Y') {
                    end = new Point(i, j);
                }
            }
        }

        if (start == null || end == null) {
            System.out.println("Start or end point not found in the maze.");
            return;
        }

        int minSteps = bfs(maze, start, end);
        if (minSteps != -1) {
            System.out.println("Minimum steps to reach the endpoint: " + minSteps);
        } else {
            System.out.println("No path found to reach the endpoint.");
        }

        // Visualize the grid
System.out.println("Grid:");
for (int i = 0; i < maze.length; i++) {
    for (int j = 0; j < maze[0].length; j++) {
        System.out.print(maze[i][j] + " ");
    }
    System.out.println();

}
// Visualize the shortest path
System.out.println("Shortest Path:");
Point current = end;
while (current != start) {
    System.out.print("(" + current.x + ", " + current.y + ") -> ");
    int nx = current.x;
    int ny = current.y;
    for (int j = 0; j < 4; j++) {
        int px = nx - dx[j];
        int py = ny - dy[j];
        if (px >= 0 && px < n && py >= 0 && py < m && maze[px][py] != '1' && visited[px][py] && steps - 1 == bfs(maze, new Point(px, py), current)) {
            nx = px;
            ny = py;
            break;
        }
    }
    current = new Point(nx, ny);
}
System.out.println("(" + start.x + ", " + start.y + ")");
    

}}