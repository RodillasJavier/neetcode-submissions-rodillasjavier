from collections import defaultdict
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
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in nums:
                continue

            j = 0
            while num + j in nums:
                j += 1
            
            longest = max(longest, j)
        
        return longest