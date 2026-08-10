from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        in:
            - n x n binary matrix
        out:
            - return the length of the shortest clear path in the matrix
            - return -1 if there is no clear path
        constraints:
            - clear path => path from top left cell to bottom right s.t.
                - all visited c ells are 0
                - all cells of the path share either an edge or a corner
        """
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        length = 1
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
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            length += 1 
        
        return -1


# time complexity: O(r * c)
# space complexity: O(r * c)