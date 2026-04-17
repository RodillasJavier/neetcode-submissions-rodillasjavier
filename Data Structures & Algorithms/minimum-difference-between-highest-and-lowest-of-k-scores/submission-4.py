class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        in:
            - int[] nums
            - int k
        out:
            - choose k ele s.t.
            - min(highest - lowest)
        constraints:
            - 1 <= k <= len(nums) <= 1,000
            - 0 <= nums[i] <= 100,000
        edge cases:
            - len(nums) or k == 1? k - 0?
        '''


        nums.sort()
        min_diff = nums[k - 1] - nums[0]
        for R in range(k, len(nums)):
            curr_diff = nums[R] - nums[R - k + 1]
            min_diff = min(min_diff, curr_diff)
        
        return min_diff


# time complexity: O(n * log(n))
# space complexity: O(1)