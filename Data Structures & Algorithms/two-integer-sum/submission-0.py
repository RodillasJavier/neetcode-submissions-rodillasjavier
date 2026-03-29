from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        in:
            - int[] nums
            - int target
        out:
            - indices i, j s.t. 
                nums[i] + nums[j] == target
                and i != j
        constraints:
            -  each input has one valid pair of indices (i, j)
        '''
        numbers = dict()

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in numbers:
                return [numbers[complement], i]
            
            numbers[num] = i