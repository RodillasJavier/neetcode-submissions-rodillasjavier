class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        in:
            - int array nums
                - nums[i] = amount of money the ith house has
        out:
            - return the max amt of money you can rob
        constraints:
            - cannot rob two adjacent houses
            - 1 <= n <= 100
            - 0 <= nums[i] <= 100
        """
        cache = {}
        n = len(nums) - 1

        def dp(n):
            if n == 0:
                return nums[0]
            
            if n == 1:
                return max(nums[0], nums[1])
            
            if n in cache:
                return cache[n]

            cache[n] = max(nums[n] + dp(n - 2), dp(n - 1))
            return cache[n]

        return dp(n)