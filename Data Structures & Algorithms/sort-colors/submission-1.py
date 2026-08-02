class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        in:
            - nums[]
                - each el represents a color
                - 0 => red
                - 1 => white
                - 2 => blue
        out:
            - sort the array in place s.t.
                - el of the same color are grouped together
                - arranged in order red (0) -> white (1) -> blue (2)
        constraints:
            - Do not return anything, modify nums in-place instead.
            - don't use built in sort
            - 1 <= n <= 300
        """
        count = [0] * 3

        for color in nums:
            count[color] += 1

        i = 0
        for color in range(len(count)):
            frequency = count[color]

            for _ in range(frequency):
                nums[i] = color
                i += 1


# time complexity: O(n)
# space complexity: O(1)
