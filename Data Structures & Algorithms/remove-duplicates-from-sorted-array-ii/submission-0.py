class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        in:
            - integer array nums
                - sorted non-decreasing
        out:
            - remove dupes in place
                - s.t. each uniq el appears at most twice
            - return k, where the res is the first k slots of nums
        constraints:
            - relative order preserved
            - result stored in the first part of nums
        '''
        read, write = 0, 0
        while read < len(nums):
            count = 1

            while read < len(nums) - 1 and nums[read] == nums[read + 1]:
                read += 1
                count += 1

            for i in range(min(2, count)):
                nums[write] = nums[read]
                write += 1
            
            read += 1

        return write
