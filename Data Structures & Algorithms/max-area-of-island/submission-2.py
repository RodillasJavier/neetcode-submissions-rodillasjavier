class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        in:
            - 2d matrix grid
                - grid[i] = 0 => water
                - grid[i] = 1 => land
        out:
            - return the maximum area of an island in grid
            - if no island exists, return 0
        """
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        max_area = 0

        to_visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    to_visit.add((r, c))

        def dfs(sr, sc):
            if not 0 <= sr < ROWS or not 0 <= sc < COLS:
                return 0
            elif grid[sr][sc] == 0 or (sr, sc) not in to_visit:
                return 0
            
            to_visit.discard((sr, sc))

            area = 1
            for dr, dc in DIRECTIONS:
                area += dfs(sr + dr, sc + dc)
            
            return area

        while to_visit:
            sr, sc = to_visit.pop()
            area = 1

            for dr, dc in DIRECTIONS:
                area += dfs(sr + dr, sc + dc)
            
            max_area = max(area, max_area)

        return max_area