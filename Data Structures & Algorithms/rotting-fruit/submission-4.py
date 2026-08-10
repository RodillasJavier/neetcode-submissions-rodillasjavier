from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        in:
            - 2d matrix grid
                - 0 => empty cell
                - 1 => fresh fruit
                - 2 => rotten fruit
        out:
            - return the min number of min that must elapse until there are
                zero fresh fruit left
            - return -1 if this is impossible
        constraints:
            - each min:
                - if a fruit is Horiz. or vert. adjacent to rotten fruit it
                    becomes rotten
            - 1 <= rows, cols, <= 10
        """
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()
        visited = set()
        fresh_fruit, rotten_fruit = 0, 0

        # enqueue all rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                    rotten_fruit += 1
                elif grid[r][c] == 1:
                    fresh_fruit += 1

        if fresh_fruit == 0:
            return 0

        minute = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        fresh_fruit -= 1

            minute += 1

            if fresh_fruit == 0:
                return minute

        return -1
