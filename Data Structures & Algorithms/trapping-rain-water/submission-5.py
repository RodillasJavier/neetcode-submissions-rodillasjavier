class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        in:
            - int[] height
        out:
            - total area of water that can be trapped between the bars
        constraints:
            - 1 <= height.length <= 1000
            - 0 <= height[i] <= 1000
        edge cases:
            - height.length <= 2 : return 0
            - strictly increasing/decreasing : ret 0
            - all equal : ret 0
        '''
        if len(height) <= 2:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
        
        return total_water

# time complexity: O(n)
# space complexity: O(1)