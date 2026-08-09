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
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        START = (0, 0)
        END = (ROWS - 1, COLS - 1)
        queue = deque()
        visited = set()
        length = 0

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        
        queue.append(START)

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) == END:
                    return length

                inbounds = 0 <= r < ROWS and 0 <= c < COLS
                if not inbounds or grid[r][c] == 1:
                    continue
                
                for dr, dc in DIRECTIONS:
                    if (r + dr, c + dc) not in visited:
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            
            length += 1

        return -1