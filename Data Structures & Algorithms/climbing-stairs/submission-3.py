class Solution:
    def climbStairs(self, n: int) -> int:
        """
        in:
            - int n => num steps to reach the top of a staircase
        out:
            - return num distinct wys to climb to the top of the staircase
        constraints:
            - can climb w/1 or 2 steps at a time
            - 1 <= n <= 45
        """
        cache = {1 : 1, 2 : 2}

        def dp(n):
            if n in cache:
                return cache[n]
            
            cache[n] = dp(n - 1) + dp(n - 2)
            return cache[n]
        
        return dp(n)


# time complexity: O(n)
# space complexity: O(n)