class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = False
        zeroIdx = None
        for i, num in enumerate(nums):
            if num == 0 and hasZero:
                return [0] * len(nums)
            elif num == 0:
                hasZero = True
                zeroIdx = i
            else:
                product *= num
        
        if hasZero:
            nums = [0] * len(nums)
            nums[zeroIdx] = product
            return nums


        for i in range(len(nums)):
            nums[i] = int(product / nums[i])
                
        return nums        

# Time complexity: O(n)
# Space complexity: O(1)