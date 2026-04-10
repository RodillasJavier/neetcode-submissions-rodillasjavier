class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        in:
            - int[] numbers
                - sorted non decreasing
            - int target
        out:
            - indices of two numbers [i1, i2] s.t.
                - sum to target
                - i1 < i2
                - 1 based
        constraints:
            - i1 and i2 cannot be equal
            - will always be one valid solution
            - O(1) space
        '''
        left, right = 0, len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]

            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                return [left + 1, right + 1]

# time complexity: O(n)
# space complexity: O(1)