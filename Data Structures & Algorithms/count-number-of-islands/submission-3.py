class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        in:
            - 2d grid
                - 1 => land
                - 0 => water
        out:
            - return the number of islands
        constraints:
            - 1 <= rows, cols <= 100
            - grid[i][j] is either '0' or '1'
        """
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        to_visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    to_visit.add((r, c))
        
        print(to_visit)

        def dfs(sr, sc):
            if not 0 <= sr < ROWS or not 0 <= sc < COLS:
                return
            elif grid[sr][sc] == '0' or (sr, sc) not in to_visit:
                return

            to_visit.discard((sr, sc))

            for dr, dc in DIRECTIONS:
                dfs(sr + dr, sc + dc)

        num_islands = 0
        while to_visit:
            sr, sc = to_visit.pop()

            num_islands += 1
            
            for dr, dc in DIRECTIONS:
                dfs(sr + dr, sc + dc)
        
        return num_islands