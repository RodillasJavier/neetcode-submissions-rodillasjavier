class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        in:
            - nums[]
                - sorted ascending
            - int target
        out:
            - search for target in nums
            - iff exists index, else -1
        constraints:
            - O(log n) time
            - 1 <= n <= 10000
            - -10000 <= nums[i], target <= 10000
            - all ints in nums are unique
        edge cases:
            - element DNE in array
            - element at the ends of the array
        """
        L, R = 0, len(nums) - 1
        mid = (L + R) // 2

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] < target:
                L = mid + 1

            elif nums[mid] > target:
                R = mid - 1

            else:
                break

        if nums[mid] == target:
            return mid
        else:
            return -1


# time complexity: O()
# space complexity: O()