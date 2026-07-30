class Solution:
    def climbStairs(self, n: int) -> int:
        """
        in:
            - integer n : num steps to reach top of stairs
        out:
            - return num distinct ways to climb to the top of the stairs
        constraints:
            - can climb with either 1 or 2 steps at a time
            - 1 <= n <= 45
            - order matters (i.e. 1 + 2 != 2 + 1)
        """
        memo = {}

        def dfs(steps):
            """helper to recursively calculate steps needed"""
            # Base case
            if steps <= 2:
                return steps

            # Memoize this case (if applicable)
            if steps not in memo:
                memo[steps] = dfs(steps - 1) + dfs(steps - 2)

            # Surface the answer for this step
            return memo[steps]

        return dfs(n)

# time complexity: O(n)
# space complexity: O(n)