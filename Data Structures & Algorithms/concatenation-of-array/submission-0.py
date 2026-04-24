class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        in:
            - int[] nums
        out:
            - int[] ans
                - length 2n
                - ans[i] == nums[i]
                - ans[i + n] == nums[i]
        '''
        ans = [1] * (len(nums) * 2)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]

        return ans