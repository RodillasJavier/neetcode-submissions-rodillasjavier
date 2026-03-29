class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        in: 
            - int[] nums
        out:
            - true iff duplicates
            - false o/w
        '''
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        
        return False