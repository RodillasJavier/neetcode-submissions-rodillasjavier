from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        in:
            - nums: int[]
        out:
            - all triplets [nums[i], nums[j], nums[k]]: int[][]
            - s.t. they sum to 0
        constraints:
            - i, j, k all distinct
            - no duplicate triplets
            - 3 <= len(nums) <= 1000
        '''
        res = []
        nums = sorted(nums)

        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                threesum = number + nums[left] + nums[right]

                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([number, nums[left], nums[right]])

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return res