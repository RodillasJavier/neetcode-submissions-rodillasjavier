class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        in:
            - int[] heights
            - heights[i] = height of a bar (wid = 1)
        out:
            - area of the largest rectangle that can be formed
        constraints:
            - 1 <= heights.length <= 1000
            - 0 <= heights[i] <= 1000
        '''
        stack = []  # (index, height)
        largest_area = 0

        for index, height in enumerate(heights):
            start = index

            while stack and stack[-1][1] > height:
                idx, ht = stack.pop()

                new_area = (index - idx) * ht
                largest_area = max(largest_area, new_area)

                start = idx
            
            stack.append((start, height))
        
        for index, height in stack:
            new_area = (len(heights) - index) * height
            largest_area = max(largest_area, new_area)
        
        return largest_area