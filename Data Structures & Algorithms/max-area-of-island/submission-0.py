class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        in:
            - grid
                - grid[i] = 1 => land
                - grid[i] = 0 => water
        out:
            - max area of an island in grid
            - if none, return 0
        cosntraints:
            - 1 <= rows, cols <= 50
        '''
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def getArea(row, col):
            if not (0 <= row < ROWS) or not (0 <= col < COLS) or grid[row][col] == 0:
                return 0
            
            area = 1
            grid[row][col] = 0
            for dr, dc in DIRS:
                area += getArea(row + dr, col + dc)
            
            return area
        
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, getArea(row, col))

        return max_area