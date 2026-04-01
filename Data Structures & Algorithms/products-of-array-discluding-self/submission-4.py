class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        pre = [1] * len(nums)
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            pre[i] = product
        
        product = 1
        post = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            post[i] = product
        
        for i in range(len(nums)):
            nums[i] = pre[i] * post[i]

        return nums

# Time complexity: O(n)
# Space complexity: O(n)