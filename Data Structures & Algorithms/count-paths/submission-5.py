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

        prev_row = [0] * n
        for i in range(m):
            curr_row = [0] * n
            curr_row[-1] = 1

            for j in range(n - 2, -1, -1):
                curr_row[j] = curr_row[j + 1] + prev_row[j]

            prev_row = curr_row

        return curr_row[0]


# time complexity: O(m * n)
# space complexity: O(1)
