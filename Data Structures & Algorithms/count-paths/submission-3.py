class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        in:
            - int m
            - int n
        out:
            - return the num possible unique paths from origin to bot right
        constraints:
            - 1 <= m, n <= 100
            - can move either down or to the right
        """
        rows, cols = m, n
        cache = {}
        for i in range(m):
            for j in range(n):
                cache[(i, j)] = 0

        def dp(r, c):
            if r == rows or c == cols:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1

            if cache[(r, c)] > 0:
                return cache[(r, c)]

            cache[(r, c)] = dp(r + 1, c) + dp(r, c + 1)
            return cache[(r, c)]

        return dp(0, 0)


# time complexity: O(m * n)
# space complexity: O(m * n)
