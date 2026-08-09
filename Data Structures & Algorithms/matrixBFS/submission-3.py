from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        """
        in:
            - binary tree matrix Grid
                - 0 => land
                - 1 => rocks (cannot be traversed)
        out:
            - return the length of the SP from origin to bottom right corner
            - return -1 if there is not such path
        constraints:
            - all traversed cells are land cells (i.e. 0)
            - only move vertically or horizontally
            - length of SP is num of moves from starting cell to ending cell
                - num cells - 1
        """
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        length = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) == (ROWS - 1, COLS - 1):
                    return length
                
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 0
                        and (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            length += 1

        return -1