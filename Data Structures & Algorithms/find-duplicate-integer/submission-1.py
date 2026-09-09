class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        in: 
            - int array nums
                - n + 1 numbers
                - exactly 1 duplicate in the range [1, n]
        out:
            - return the repeated integer
        """
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        
        return 0