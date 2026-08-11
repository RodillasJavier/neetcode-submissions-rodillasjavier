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
        prev_max, curr_max = 0, 0
        for money in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + money)
            prev_max = temp

        return curr_max


# time complexity: O(n)
# space complexity: O(1)
