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
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


# Time complexity: O(n)
# Space complexity: O(1)