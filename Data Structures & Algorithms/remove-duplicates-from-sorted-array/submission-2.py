class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        in: 
            - int array nums
                - sorted non-decr.
        out:
            - remove duplicates from nums in-place
                - s.t. each element appears only once
            - return num of unique elements as k
        '''
        write = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[write] = nums[i]
                write += 1
        
        return write