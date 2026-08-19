import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        in:
            - pos int array nums
            - pos int target
        out:
            - return min length of a subarr s.t.
                - sum >= target
            - return 0 if no such subarr exists
        constraints:
            - 1 <= n <= 100,000
            - 1 <= nums[i] <= 10,000
            - 1 <= target <= inf
        '''
        minimum = math.inf

        L, total = 0, 0
        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                minimum = min(minimum, R - L + 1)
                total -= nums[L]
                L += 1
        
        if minimum is not math.inf:
            return minimum
        else:
            return 0
            
