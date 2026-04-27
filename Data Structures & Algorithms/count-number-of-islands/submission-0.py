class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        in:
            - 2d grid
                - '1' => land
                - '0' => water
        out:
            - num of islands
        constraints:
            - 1 <= len(grid), len(grid[i]) <= 100
        '''
        total_islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            '''
            in:
                - starting row
                - starting col
            out:
                - turn each connected row / col that is a '1' into a '0'
            '''
            if not (0 <= row < ROWS) or not (0 <= col < COLS) or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                curr = grid[row][col]
                if curr == '0':
                    continue
                
                dfs(row, col)
                total_islands += 1
        
        return total_islands