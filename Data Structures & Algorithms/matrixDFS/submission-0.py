class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        """
        in:
            - binary matrix grid
                - 0 => land
                - 1 => rocks that can't be traversed
        out:
            - num of unique paths from top left to bottom right
        constraints:
            - all traversed cells must be land cells (0)
            - cannot visit the same cell twice on a unique individual path
        """
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(grid, row=0, col=0, visited=set()):
            nonlocal ROWS, COLS, DIRECTIONS

            if (
                min(row, col) < 0 or 
                row == ROWS or col == COLS or 
                grid[row][col] == 1 or 
                (row, col) in visited
            ):
                return 0
            
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            visited.add((row, col))
            count = 0

            for dr, dc in DIRECTIONS:
                path = dfs(grid, row + dr, col + dc, visited)
                count += path
            
            visited.discard((row, col))
            return count

        return dfs(grid)