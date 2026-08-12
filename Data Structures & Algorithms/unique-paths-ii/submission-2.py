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
        cache = {}
        for r in range(rows):
            for c in range(cols):
                cache[(r, c)] = 0

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1

            if cache[(r, c)] > 0:
                return cache[(r, c)]

            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)


# time complexity: O(r * c)
# space complexity: O(r * c)
