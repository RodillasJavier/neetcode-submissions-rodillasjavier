class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        in:
            - m x n int array grid
        out:
            - num possible unique paths from origin to bot right
        constraints:
            - can only move down or right at any time
            - can't move on 1s, but can on 0s
            - 1 <= m, n <= 100
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * cols
        prev_row[-1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c] == 1:
                    prev_row[c] = 0
                elif c + 1 < cols:
                    prev_row[c] = prev_row[c] + prev_row[c + 1]
                
        return prev_row[0]