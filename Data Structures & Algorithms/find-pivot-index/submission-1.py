class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        in:
            - int[] nums
        out:
            - leftmost pivot index of array
            - idx s.t.
                - sum of all num left == " " " " right
                - left edge => left = 0
                - right edge => right = 0
        edge cases:
            - if no solution exists => ret -1
        constraints:
            - 1 <= n <= 10,000
            - 1000 <= nums[i] <= 1000
        '''
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            current = nums[i]

            right = total - left - current
            if left == right:
                return i

            left += current

        return -1