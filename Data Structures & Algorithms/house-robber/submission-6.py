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
        max_amt = [0, 0]
        for num in nums:
            temp = max_amt[1]
            max_amt[1] = max(max_amt[1], max_amt[0] + num)
            max_amt[0] = temp

        return max_amt[1]


# time complexity: O(n)
# space complexity: O(1)
