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
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i + 1])
                continue
            
            i += 1
        
        return len(nums)