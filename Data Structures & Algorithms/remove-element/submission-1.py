class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        in:
            - int[] nums
            - int val
        out:
            - remove in place all occurences of val from nums
            - return num of remaining elements k s.t.
                - first k ele do not contain val
        edge cases:
            - 0 <= n <= 100
            - 0 <= nums[i] <= 50
            - 0 <= target <= 100
        '''
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            
            i += 1
        
        return len(nums)


# Time complexity: O(n)
# Space complexity: O(1)