class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        in:
            - int array nums
                - rotated between 1 and n times
            - int target
        out:
            - return index if target in nums, or -1
        constraints:
            - all elements in nums are unique
            - O(log n) time
            - 1 <= n <= 1000
            - nums[i], target can be pos or neg
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# time complexity: O(log n)
# space complexity: O(1)
