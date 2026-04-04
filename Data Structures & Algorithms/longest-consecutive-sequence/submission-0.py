class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        in:
            - int[] nums
        out:
            - length of longest consec. sequence of el
            - each el is 1 greater than prev
            - don't have to be consecutive in the OG array
        constraints:
            - 0 <= n <= 1000
            - O(n) runtime
        '''
        if not nums:
            return 0

        vals = set()
        mn, mx = nums[0], nums[0]
        for num in nums:
            vals.add(num)
            mn = min(num, mn)
            mx = max(num, mx)
        
        longest = 1
        current = 1
        for i in range(mn + 1, mx + 1, 1):
            if i in vals:
                current += 1
            else:
                longest = max(longest, current)
                current = 0
        
        longest = max(longest, current)
        return longest