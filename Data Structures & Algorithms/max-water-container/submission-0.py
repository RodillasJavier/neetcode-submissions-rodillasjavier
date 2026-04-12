class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        in:
             - int[] heights
             - heights[i] = height of the ith bar
        out:
            - maximum amount of water a container can store
        constraints:
            - 2 <= height.length <= 1000
            - 0 <= height[i] <= 1000
        edge cases:
            - only 2 bars
        '''
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area