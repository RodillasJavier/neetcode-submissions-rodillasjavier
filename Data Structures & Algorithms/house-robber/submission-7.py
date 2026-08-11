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
        max_0, max_1 = 0, 0
        for num in nums:
            temp = max_1
            max_1 = max(max_1, max_0 + num)
            max_0 = temp

        return max_1


# time complexity: O(n)
# space complexity: O(1)
