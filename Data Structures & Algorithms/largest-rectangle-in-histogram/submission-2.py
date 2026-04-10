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
        heights.append(0)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, ht = stack.pop()

                new_area = (i - idx) * ht
                largest_area = max(largest_area, new_area)

                start = idx
            
            stack.append((start, h))
        
        return largest_area