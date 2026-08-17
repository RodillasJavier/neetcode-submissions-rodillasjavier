class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        in:
            - int[] nums
            - int k
        out:
            - true iff 2 distinct indices i & j s.t.
                - nums[i] == nums[j]
                - abs(i - j) <= k
            - false o/w
        constraints:
            - 1 <= nums.length <= 100,000
            - -1,000,000,000 <= nums[i] <= 1,000,000,000
            - 0 <= k <= 100,000
        """
        window = set()

        left = 0
        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False


# time complexity: O(n)
# space complexity: O(n)
