class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        in:
            - int[] nums
            - int k
        out:
            - a subarray of k elements s.t.
            - min(highest - lowest)
        constraints:
            - 1 <= k <= len(nums) <= 1,000
            - 0 <= nums[i] <= 100,000
        edge cases:
            - len(nums) or k == 1? k - 0?
        '''
        if k == 1:
            return 0

        nums = sorted(nums)
        min_diff = nums[k - 1] - nums[0]
        for R in range(k, len(nums)):
            curr_diff = nums[R] - nums[R - k + 1]
            min_diff = min(min_diff, curr_diff)
        
        return min_diff


'''
nums = [2,5,3,1,6,3], k = 3
253163 | k = 3

012345 index
123356 | k = 3
LXR000 | res = 2
0LXR00 | res = 1
00LXR0 | res = 1
000LXR | res = 1

---

Input: nums = [9,4,1,7], k = 2
9417 | k = 2
1479 | k = 2

1479 | k = 2
LR00 | res = 3
0LR0 | res = 3
00LR | res = 2
'''
