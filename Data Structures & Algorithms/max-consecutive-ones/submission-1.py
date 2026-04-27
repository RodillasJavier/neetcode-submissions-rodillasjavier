class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        in:
            - bin array nums
        out:
            - max num consecutive ones in the array
        constraints:
            - 1 <= n <= 100,000
            - each val either 1 or 0
        '''
        res = 0
        current = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                res = max(res, current)
                current = 0
        
        return max(current, res)


# time complexity: O(n)
# space complexity: O(1)